from fastapi import APIRouter
from ...schemas.ai import AIAnalyzeRequest, AIAnalyzeResponse
from ...services.ai_prompt import build_prompt

router = APIRouter()

@router.post("/analyze", response_model=AIAnalyzeResponse)
def analyze(payload: AIAnalyzeRequest):
    prompt = build_prompt(user_id=payload.user_id)
    return {
        "risk_score": 72,
        "risk_level": "中高风险",
        "concentration_analysis": "持仓集中度偏高",
        "correlation_analysis": "与沪深300相关性偏高",
        "suggestion_direction": "降低单一行业仓位",
        "risk_warning": "不构成投资建议，市场波动存在风险",
    }