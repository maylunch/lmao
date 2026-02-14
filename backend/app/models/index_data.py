from sqlalchemy import String, Date, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from ..core.database import Base

class IndexData(Base):
    __tablename__ = "index_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    index_code: Mapped[str] = mapped_column(String(20))
    index_name: Mapped[str] = mapped_column(String(50))
    date: Mapped[str] = mapped_column(Date)
    close_price: Mapped[float] = mapped_column(DECIMAL(20, 4))