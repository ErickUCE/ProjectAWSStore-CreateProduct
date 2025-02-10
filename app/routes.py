from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.productController import create_product
from app.schemas import ProductCreate


router = APIRouter()

@router.post("/products", status_code=201)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)

