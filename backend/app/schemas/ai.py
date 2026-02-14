from pydantic import BaseModel

class AIAnalyzeRequest(BaseModel):
    user_id: int

class AIAnalyzeResponse(BaseModel):
    risk_score: int
    risk_level: str
    concentration_analysis: str
    correlation_analysis: str
    suggestion_direction: str
    risk_warning: str