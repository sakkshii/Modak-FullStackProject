from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schema.order_schema import OrderCreate, OrderResponse
from app.services import order_service

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post( "", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(data:OrderCreate, db:Session=Depends(get_db)):
    return order_service.create_order(db, data)
