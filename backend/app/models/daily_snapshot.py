from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from ..core.database import Base

class DailySnapshot(Base):
    __tablename__ = "daily_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("positions.id"), index=True)
    date: Mapped[str] = mapped_column(Date)
    close_price: Mapped[float] = mapped_column(DECIMAL(20, 4))
    market_value: Mapped[float] = mapped_column(DECIMAL(20, 4))
    unrealized_pnl: Mapped[float] = mapped_column(DECIMAL(20, 4))