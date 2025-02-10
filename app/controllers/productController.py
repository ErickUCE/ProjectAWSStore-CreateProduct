from sqlalchemy.orm import Session
from app.models import Product
from app.utils import validar_proveedor
from app.schemas import ProductCreate

def create_product(product: ProductCreate, db: Session):
    """Crea un nuevo producto con el nombre del proveedor en lugar del ID."""
    
    # 🔹 Obtener el nombre del proveedor usando el ID
    nombre_proveedor = validar_proveedor(product.proveedor_id)

    db_product = Product(
        nombreProducto=product.nombreProducto,
        descripcion=product.descripcion,
        marca=product.marca,
        precio=product.precio,
        proveedor_id=product.proveedor_id,  # 🔥 Sigue almacenando el ID
        proveedor_nombre=nombre_proveedor  # ✅ Nuevo campo con el nombre del proveedor
    )
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product
