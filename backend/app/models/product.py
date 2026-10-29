from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from sqlalchemy import String
from decimal import Decimal
from sqlalchemy import Numeric, Boolean


class Product(Base):
    __tablename__ = "products"

    product_id:Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    product_name:Mapped[str] = mapped_column(String(100), nullable=False)
    price:Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)



