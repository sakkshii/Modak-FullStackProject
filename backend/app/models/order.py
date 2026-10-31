from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, Time, func
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from datetime import date, datetime, time 

from app.database.base import Base

class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column( ForeignKey("customers.customer_id"), nullable=False)
    accepted_by:Mapped[int | None] = mapped_column(ForeignKey("admins.admin_id"))
    created_at: Mapped[datetime]= mapped_column(DateTime, server_default=func.now(), nullable=False)
    accepted_at:Mapped[datetime|None]=mapped_column(DateTime)
    pickup_date:Mapped[date]=mapped_column(Date,nullable=False)
    pickup_time:Mapped[time]=mapped_column(Time,nullable=False)
    total_amount:Mapped[Decimal]=mapped_column(Numeric(10, 2), nullable=False)
    order_status: Mapped[str]=mapped_column(String(20), default="PENDING", nullable=False)
    