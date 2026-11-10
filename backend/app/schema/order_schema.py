from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import date, time
from decimal import Decimal

class OrderProduct(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int =Field(gt=0)

class OrderCreate(BaseModel):
    name:str = Field(min_length=1, max_length=100)
    email:EmailStr
    phone:str | None = Field(default=None, max_length=20)
    address:str|None=Field(default=None, max_length=255)
    pickup_date:date
    pickup_time:time
    items: list[OrderProduct] = Field(min_length=1)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value:str)->str:
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        return value

class OrderResponse(BaseModel):
    order_id :int
    total_amount: Decimal
    order_status : str
    pickup_date: date
    pickup_time : time 

    
   