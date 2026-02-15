from __future__ import annotations

import json
from typing import Any, Dict

import httpx

from ..core.config import settings


class AIClient:
    def __init__(self) -> None:
        self.base_url = settings.AI_API_URL
        self.api_key = settings.AI_API_KEY
        self.model = settings.AI_MODEL
        self.timeout = 20.0

    def analyze(self, prompt: str) -> Dict[str, Any]:
        if not self.base_url or not self.api_key:
            return {}

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "你是一名专业投资风险分析助手。"},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}

        with httpx.Client(timeout=self.timeout) as client:
            response = client.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        content = ""
        if isinstance(data, dict):
            choices = data.get("choices", [])
            if choices:
                content = choices[0].get("message", {}).get("content", "")

        if not content:
            return {}

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"raw": content}