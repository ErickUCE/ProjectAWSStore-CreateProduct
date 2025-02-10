from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.productController import create_product
from app.schemas import ProductCreate
from app.controllers.productController import sync_update_product



router = APIRouter()

@router.post("/products", status_code=201)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)


# 📌 Endpoint para recibir actualizaciones desde `UpdateProduct`
@router.post("/sync-update")
def sync_product_update(product_data: dict, db: Session = Depends(get_db)):
    return sync_update_product(product_data, db)