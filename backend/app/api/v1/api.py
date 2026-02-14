from fastapi import APIRouter
from .endpoints import auth, vip, position, portfolio, chart, ai

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(vip.router, prefix="/vip", tags=["vip"])
api_router.include_router(position.router, prefix="/position", tags=["position"])
api_router.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
api_router.include_router(chart.router, prefix="/chart", tags=["chart"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])