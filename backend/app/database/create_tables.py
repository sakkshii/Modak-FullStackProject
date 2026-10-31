from app.database.base import Base
from app.database.connection import engine

from app.models.product import Product
from app.models.admin import Admin
from app.models.customer import Customer
from app.models.order import Order
from app.models.order_detail import OrderDetail
from app.models.payment import payment


def create_tables():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

if __name__ == "__main__":
    create_tables()
    