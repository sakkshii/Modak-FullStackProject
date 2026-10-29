from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.product import Product

products = [
        {
        "product_id": 1,
        "product_name":"Chocolate Modak",
        "price":"3.00",
        "is_available":True 
        },

        {
        "product_id": 2,
        "product_name":"Mango Modak",
        "price":"3.00",
        "is_available":True 
        },

        {
        "product_id": 3,
        "product_name":"Kesar",
        "price":"2.30",
        "is_available":True 
        }
    ]

def get_all_products(db:Session):
    statement = select(Product).order_by(Product.product_id)
    return db.scalars(statement).all()
def get_product_by_id(db:Session, product_id : int):
    return db.get(Product, product_id)
