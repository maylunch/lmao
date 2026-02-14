from fastapi import APIRouter
from ...schemas.portfolio import PortfolioSummary

router = APIRouter()

@router.get("/summary", response_model=PortfolioSummary)
def summary():
    return {
        "total_asset": 1000000,
        "today_pnl": 2300,
        "total_return": 0.23,
        "risk_score": 72,
    }