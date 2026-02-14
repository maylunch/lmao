from sqlalchemy import String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from ..core.database import Base

class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), index=True)
    stock_code: Mapped[str] = mapped_column(String(20))
    market: Mapped[str] = mapped_column(String(20))
    quantity: Mapped[float] = mapped_column(DECIMAL(20, 4))
    avg_cost: Mapped[float] = mapped_column(DECIMAL(20, 4))
    leverage_ratio: Mapped[float] = mapped_column(DECIMAL(10, 4), default=1.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)