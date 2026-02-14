from fastapi import APIRouter
from ...schemas.payment import CreateOrderRequest

router = APIRouter()

@router.post("/order")
def create_order(payload: CreateOrderRequest):
    return {"order_no": "VIP2026XXXXX", "status": "Created"}