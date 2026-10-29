from fastapi import APIRouter, HTTPException, Depends
from app.services import product_service

from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.schema.product_schema import ProductResponse

router = APIRouter(prefix="/products", tags= ["Products"])

@router.get("", response_model=list[ProductResponse])
def get_products(db:Session=Depends(get_db)): #FastAPI’s way of saying “give me a database connection for this request.” get_db opens the connection and closes it once the request is finished.
    return product_service.get_all_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id:int, db:Session = Depends(get_db)): 
    #FastAPI’s way of saying “give me a database connection for this request.” get_db opens the connection and closes it once the request is finished.
    product = product_service.get_product_by_id(db,product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
