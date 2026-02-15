from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import hmac
import json
from typing import Any, Dict

import redis

from ..core.config import settings

ORDER_KEY_PREFIX = "pay:order:"
NONCE_KEY_PREFIX = "pay:nonce:"

@dataclass
class PaymentResult:
    order_no: str
    status: str
    message: str


class PaymentService:
    def __init__(self) -> None:
        self.redis = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

    def create_order(self, user_id: int, amount: float, pay_channel: str) -> Dict[str, Any]:
        order_no = f"VIP{datetime.utcnow().strftime('%Y%m%d%H%M%S')}{user_id}"
        key = f"{ORDER_KEY_PREFIX}{order_no}"
        self.redis.hset(
            key,
            mapping={
                "status": "Pending",
                "amount": amount,
                "pay_channel": pay_channel,
                "user_id": user_id,
            },
        )
        self.redis.expire(key, 86400)
        return {"order_no": order_no, "status": "Pending"}

    def process_callback(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        signature = payload.pop("signature", "")
        if not self._verify_signature(payload, signature):
            return self._result(payload.get("order_no", ""), "Rejected", "Invalid signature")

        if not self._check_timestamp(payload.get("timestamp")):
            return self._result(payload.get("order_no", ""), "Rejected", "Timestamp invalid")

        if not self._check_nonce(payload.get("nonce", "")):
            return self._result(payload.get("order_no", ""), "Rejected", "Replay detected")

        order_no = payload.get("order_no", "")
        if not order_no:
            return self._result("", "Rejected", "Missing order number")

        key = f"{ORDER_KEY_PREFIX}{order_no}"
        if not self.redis.exists(key):
            return self._result(order_no, "NotFound", "Order not found")

        current_status = self.redis.hget(key, "status") or "Pending"
        if current_status == "Paid":
            return self._result(order_no, "Paid", "Already paid")

        incoming_status = payload.get("status", "")
        if incoming_status.lower() in {"paid", "success", "succeeded"}:
            self.redis.hset(key, mapping={"status": "Paid", "paid_at": datetime.utcnow().isoformat()})
            return self._result(order_no, "Paid", "Payment confirmed")

        self.redis.hset(key, mapping={"status": "Failed"})
        return self._result(order_no, "Failed", "Payment failed")

    def _check_nonce(self, nonce: str) -> bool:
        if not nonce:
            return False
        key = f"{NONCE_KEY_PREFIX}{nonce}"
        return bool(self.redis.set(key, "1", nx=True, ex=settings.PAY_NONCE_TTL_SECONDS))

    def _check_timestamp(self, timestamp: Any) -> bool:
        try:
            timestamp_value = float(timestamp)
        except (TypeError, ValueError):
            return False
        now = datetime.now(timezone.utc).timestamp()
        return abs(now - timestamp_value) <= settings.PAY_TIMESTAMP_TOLERANCE_SECONDS

    def _verify_signature(self, payload: Dict[str, Any], signature: str) -> bool:
        if not signature:
            return False
        message = json.dumps(payload, separators=(" , " , ":"), sort_keys=True)
        expected = hmac.new(
            settings.PAY_CALLBACK_SECRET.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return hmac.compare_digest(expected, signature)

    def _result(self, order_no: str, status: str, message: str) -> Dict[str, Any]:
        return {"order_no": order_no, "status": status, "message": message}