from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class ProductResponse(BaseModel):
    product_id: int 
    product_name: str
    price: Decimal
    is_available: bool 

    model_config = ConfigDict(from_attributes=True) #Your database layer returns a SQLAlchemy object (the Product model), not a dictionary. This setting lets Pydantic read the values straight from that object’s attributes (product.product_name, product.price and so on). Without it, Pydantic would only accept dictionaries, and passing it a database object would fail.
    