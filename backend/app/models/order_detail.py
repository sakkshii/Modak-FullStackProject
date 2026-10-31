from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from sqlalchemy import ForeignKey, Numeric

class OrderDetail(Base):
    __tablename__ = "order_details"

    detail_id:Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int]=mapped_column(ForeignKey("orders.order_id"),nullable=False)
    product_id:Mapped[int]=mapped_column(ForeignKey("products.product_id"), nullable=False)
    quantity:Mapped[int]=mapped_column(nullable=False)
    unit_price:Mapped[Decimal]=mapped_column(Numeric(10,2),nullable=False)
    