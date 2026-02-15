from fastapi import APIRouter
from ...schemas.payment import CreateOrderRequest, CreateOrderResponse, PaymentCallbackRequest, PaymentCallbackResponse
from ...services.payment import PaymentService

router = APIRouter()

@router.post("/order", response_model=CreateOrderResponse)
def create_order(payload: CreateOrderRequest):
    service = PaymentService()
    return service.create_order(
        user_id=payload.user_id,
        amount=payload.amount,
        pay_channel=payload.pay_channel,
    )

@router.post("/callback", response_model=PaymentCallbackResponse)
def payment_callback(payload: PaymentCallbackRequest):
    service = PaymentService()
    return service.process_callback(payload.model_dump())