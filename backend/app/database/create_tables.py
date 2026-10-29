from app.database.base import Base
from app.database.connection import engine

from app.models.product import Product

def create_tables():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

if __name__ == "__main__":
    create_tables()
    