from sqlalchemy import String, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from ..core.database import Base

class PaymentOrder(Base):
    __tablename__ = "payment_orders"

    order_no: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2))
    pay_channel: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)