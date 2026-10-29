from app.repository import product_repository
from sqlalchemy.orm import Session

def get_all_products(db: Session):
    return product_repository.get_all_products(db)   

def get_product_by_id(db:Session, product_id:int):
    return product_repository.get_product_by_id(db, product_id)