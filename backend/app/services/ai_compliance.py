from __future__ import annotations

from typing import Any, Dict

REQUIRED_FIELDS = {
    "risk_score": 0,
    "risk_level": "未知",
    "concentration_analysis": "暂无分析",
    "correlation_analysis": "暂无分析",
    "suggestion_direction": "暂无建议",
    "risk_warning": "不构成投资建议，市场波动存在风险",
}

def normalize_output(payload: Dict[str, Any]) -> Dict[str, Any]:
    normalized: Dict[str, Any] = {}
    for key, default in REQUIRED_FIELDS.items():
        normalized[key] = payload.get(key, default)

    if isinstance(normalized["risk_score"], str):
        try:
            normalized["risk_score"] = int(normalized["risk_score"])
        except ValueError:
            normalized["risk_score"] = REQUIRED_FIELDS["risk_score"]

    return normalized

def enforce_disclaimer(payload: Dict[str, Any]) -> Dict[str, Any]:
    payload["risk_warning"] = REQUIRED_FIELDS["risk_warning"]
    return payload
