from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ..core.database import Base

class StockMaster(Base):
    __tablename__ = "stock_master"

    stock_code: Mapped[str] = mapped_column(String(20), primary_key=True)
    stock_name: Mapped[str] = mapped_column(String(100))
    market: Mapped[str] = mapped_column(String(20))
    industry: Mapped[str] = mapped_column(String(50))
    currency: Mapped[str] = mapped_column(String(10))