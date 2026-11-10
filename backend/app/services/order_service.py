from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.admin import Admin
from app.models.customer import Customer
from app.models.order import Order
from app.models.order_detail import OrderDetail
from app.repository import order_repository
from app.schema.order_schema import OrderCreate

STORE_TZ = ZoneInfo("America/Los_Angeles")
def create_order(db:Session, data:OrderCreate):
    # validate pickup date and time 
    pickup_datetime = datetime.combine(data.pickup_date, data.pickup_time)
    if pickup_datetime.tzinfo is None:
        pickup_datetime = pickup_datetime.replace(tzinfo=STORE_TZ)
    else:
        pickup_datetime = pickup_datetime.astimezone(timezone.utc)
        
    if pickup_datetime <= datetime.now(timezone.utc):
        raise HTTPException(status_code=422, detail="Pickup must be in the future")

    # combine repeated prod ids
    quantities = {}
    for item in data.items:
        quantities[item.product_id] = (quantities.get(item.product_id, 0)+ item.quantity)

    # validate products before saving everything
    order_items= []
    total = Decimal("0.00")

    for product_id, quantity in quantities.items():
        product = order_repository.find_product(db, product_id)

        if product is None:
            raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
        if not product.is_available:
            raise HTTPException(status_code=409, detail=f"{product.product_name} is sold out")

        unit_price = product.price
        total += unit_price * quantity

        order_items.append((product, quantity, unit_price))

    try:
        customer = order_repository.find_customer_by_email(db, str(data.email))

        if customer is None:
            customer = Customer(
                name = data.name,
                email = str(data.email),
                phone = data.phone,
                address = data.address
            )
            order_repository.add_customer(db, customer)

        order = Order(
            customer_id = customer.customer_id,
            pickup_date = data.pickup_date,
            pickup_time = data.pickup_time,
            total_amount = total,
            order_status = "PENDING"
        )
        order_repository.add_order(db, order)

        for product, quantity, unit_price in order_items:
            detail = OrderDetail(
                order_id = order.order_id,
                product_id = product.product_id, 
                quantity = quantity,
                unit_price = unit_price
            )
            order_repository.add_order_details(db, detail)

        db.commit()
        db.refresh(order)
        return order
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Order could not be created due to conflicting data")
    except Exception:
        db.rollback()
        raise



    