from fastapi import APIRouter
from ...schemas.ai import AIAnalyzeRequest, AIAnalyzeResponse
from ...services.ai_prompt import build_prompt
from ...services.ai_client import AIClient
from ...services.ai_compliance import enforce_disclaimer, normalize_output

router = APIRouter()

@router.post("/analyze", response_model=AIAnalyzeResponse)
def analyze(payload: AIAnalyzeRequest):
    prompt = build_prompt(user_id=payload.user_id)
    client = AIClient()
    try:
        output = client.analyze(prompt)
    except Exception:
        output = {};

    output = normalize_output(output)
    output = enforce_disclaimer(output)
    return output