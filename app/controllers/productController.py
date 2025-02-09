from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate
from app.database import SessionLocal
from app.utils import validar_proveedor

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_product(product: ProductCreate, db: Session):
    """ Función para crear un producto con validación de proveedor """
    
    # 🔍 Validar si el proveedor existe antes de insertar el producto
    validar_proveedor(product.proveedor_id)

    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return {"message": "Producto creado exitosamente", "product": new_product}
