from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.productController import create_product
from app.schemas import ProductCreate
from app.controllers.productController import sync_update_product
from app.models import Product



router = APIRouter()

@router.post("/products", status_code=201)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)


# 📌 Endpoint para recibir actualizaciones desde `UpdateProduct`
@router.post("/sync-update")
def sync_product_update(product_data: dict, db: Session = Depends(get_db)):
    return sync_update_product(product_data, db)

@router.post("/sync-delete")
def sync_delete_product(product_data: dict, db: Session = Depends(get_db)):
    """Elimina el producto en `CreateProduct` cuando `DeleteProduct` lo notifica."""
    
    print(f"🔍 Recibiendo solicitud de eliminación: {product_data}")  # Debugging

    product_id = product_data.get("id")  # ✅ Extraer ID del producto

    if not product_id:
        print("❌ Error: ID de producto no encontrado en la solicitud")
        return {"error": "ID de producto no encontrado en la solicitud"}

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        print(f"⚠️ Producto con ID {product_id} no encontrado en CreateProduct.")
        return {"error": "Producto no encontrado en CreateProduct"}

    db.delete(product)
    db.commit()

    print(f"✅ Producto eliminado en CreateProduct: {product_id}")

    return {"message": "Producto eliminado correctamente"}

