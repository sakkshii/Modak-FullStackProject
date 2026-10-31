from decimal import Decimal
from app.database.connection import SessionLocal
from app.models.product import Product

db = SessionLocal()

try:
    chocolate = Product(
        product_name = "Chocolate Modak",
        price = Decimal("3.00"),
        is_available=True
    )
    db.add(chocolate)
    db.commit()
    print("Chocolate Modek added successfully")
finally:
    db.close()
