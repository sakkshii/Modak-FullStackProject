from app.repository import product_repository

def get_all_products():
    return product_repository.get_all_products()   

def get_product_by_id(product_id:int):

    products = product_repository.get_all_products()

    for product in products:
            if product_id == product["product_id"]:
                return product
    return None