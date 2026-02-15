from pydantic import BaseModel


class CreateOrderRequest(BaseModel):
    user_id: int
    amount: float
    pay_channel: str


class CreateOrderResponse(BaseModel):
    order_no: str
    status: str


class PaymentCallbackRequest(BaseModel):
    order_no: str
    status: str
    timestamp: float
    nonce: str
    signature: str
    amount: float | None = None
    pay_channel: str | None = None


class PaymentCallbackResponse(BaseModel):
    order_no: str
    status: str
    message: str
