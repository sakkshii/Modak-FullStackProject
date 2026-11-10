from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from app.models.order_detail import OrderDetail

def find_customer_by_email(db:Session, email:str):
    return db.scalars(
        select(Customer).where(Customer.email == email)
    ).first()
def find_product(db:Session, product_id:int):
    return db.get(Product, product_id)

def add_customer(db: Session, customer:Customer):
    db.add(customer)
    db.flush()
    return customer

def add_order(db:Session, order:Order):
    db.add(order)
    db.flush()
    return order

def add_order_details(db:Session, detail: OrderDetail):
    db.add(detail)