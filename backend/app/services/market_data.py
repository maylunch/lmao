from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

import httpx
import redis

from ..core.config import settings


class MarketDataService:
    def __init__(self) -> None:
        self.base_url = settings.MARKET_DATA_URL
        self.symbols = [s.strip() for s in settings.MARKET_FETCH_SYMBOLS.split(",") if s.strip()]
        self.redis = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

    def fetch(self) -> List[Dict[str, Any]]:
        if not self.base_url or not self.symbols:
            return []

        params = {"symbols": ",".join(self.symbols)}
        with httpx.Client(timeout=15.0) as client:
            response = client.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

        records: List[Dict[str, Any]] = []
        if isinstance(data, dict):
            payload = data.get("data") or data.get("items") or data
            if isinstance(payload, list):
                records = payload
            elif isinstance(payload, dict):
                records = [payload]

        normalized: List[Dict[str, Any]] = []
        now = datetime.now(timezone.utc).isoformat()
        for record in records:
            if not isinstance(record, dict):
                continue
            symbol = record.get("symbol") or record.get("code")
            price = record.get("price") or record.get("last")
            normalized.append({
                "symbol": symbol,
                "price": price,
                "raw": record,
                "fetched_at": now,
            })

        return normalized

    def cache_latest(self, records: List[Dict[str, Any]]) -> None:
        for record in records:
            symbol = record.get("symbol")
            if not symbol:
                continue
            key = f"market:latest:{symbol}"
            self.redis.hset(key, mapping={
                "price": record.get("price"),
                "fetched_at": record.get("fetched_at"),
                "raw": str(record.get("raw")),
            })
            self.redis.expire(key, 3600)