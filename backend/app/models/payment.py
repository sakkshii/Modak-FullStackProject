from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, Numeric, String
from datetime import datetime
from decimal import Decimal

from app.database.base import Base

class payment(Base):

    __tablename__ = "payments"

    payment_id:Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    order_id:Mapped[int]=mapped_column(ForeignKey("orders.order_id"), unique=True, nullable=False)
    amount:Mapped[Decimal]=mapped_column(Numeric(10,2), nullable=False)
    payment_method:Mapped[str]=mapped_column(String(30), nullable=False, default="QR")
    payment_status:Mapped[str]=mapped_column(String(20),nullable=False,default="PENDING")
    paid_at:Mapped[datetime|None]=mapped_column(DateTime)
    