from pydantic import BaseModel

class CreateOrderRequest(BaseModel):
    user_id: int
    amount: float
    pay_channel: str