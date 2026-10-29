from sqlalchemy.orm import DeclarativeBase

# it allows to define db tables using python classes 
# all model will inhirit from the same Base. SQLAlchemy uses the shared Base to maintain metadata about our db models. when we define the product model, SQLAlcehmy will know that it respresents a table caleed products. 
class Base(DeclarativeBase):
    pass
