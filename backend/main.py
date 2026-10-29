from fastapi import FastAPI
from app.routers import product_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Modak API"}

app.include_router(product_router.router)
