from pydantic import BaseModel

class PositionCreate(BaseModel):
    account_id: int
    stock_code: str
    market: str
    quantity: float
    avg_cost: float
    leverage_ratio: float = 1.0

class PortfolioSummary(BaseModel):
    total_asset: float
    today_pnl: float
    total_return: float
    risk_score: int