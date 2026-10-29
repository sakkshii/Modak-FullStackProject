from fastapi import APIRouter, HTTPException
from app.services import product_service

router = APIRouter()

@router.get("/products")
def get_products():
    return product_service.get_all_products()

@router.get("/products/{product_id}")
def get_product(product_id:int):

    product = product_service.get_product_by_id(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
