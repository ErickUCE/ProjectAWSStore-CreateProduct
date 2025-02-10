import decimal
from sqlalchemy.orm import Session
from app.models import Product
from app.utils import validar_proveedor
from app.schemas import ProductCreate
import os
import requests

# 🔹 URL del microservicio ReadProduct (debe estar en el .env)
READ_PRODUCT_SERVICE_URL = os.getenv("READ_PRODUCT_SERVICE_URL", "http://localhost:8002")

def create_product(product: ProductCreate, db: Session):
    """Crea un nuevo producto y lo sincroniza con ReadProduct."""

    # 🔹 Obtener el nombre del proveedor usando el ID
    nombre_proveedor = validar_proveedor(product.proveedor_id)

    # 🔥 Crear el producto en la base de datos local (CreateProduct)
    db_product = Product(
        nombreProducto=product.nombreProducto,
        descripcion=product.descripcion,
        marca=product.marca,
        precio=product.precio,  # Puede ser Decimal
        proveedor_id=product.proveedor_id,  
        proveedor_nombre=nombre_proveedor  
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    print(f"✅ Producto creado en CreateProduct: {db_product.nombreProducto}")

    # 🔄 **Sincronizar con ReadProduct**
    sync_with_read_product(db_product)

    return {
        "id": db_product.id,
        "nombreProducto": db_product.nombreProducto,
        "descripcion": db_product.descripcion,
        "marca": db_product.marca,
        "precio": float(db_product.precio),  # ✅ Convertir Decimal a float
        "proveedor_id": db_product.proveedor_id,
        "proveedor_nombre": db_product.proveedor_nombre
    }

def sync_with_read_product(product):
    """ 🔄 Enviar producto a `ReadProduct` """
    sync_url = f"{READ_PRODUCT_SERVICE_URL}/sync-create"
    product_data = {
        "id": product.id,
        "nombreProducto": product.nombreProducto,
        "descripcion": product.descripcion,
        "marca": product.marca,
        "precio": float(product.precio),  # ✅ Convertir Decimal a float
        "proveedor_id": product.proveedor_id,
        "proveedor_nombre": product.proveedor_nombre,
    }

    try:
        response = requests.post(sync_url, json=product_data)
        if response.status_code == 200:
            print(f"✅ Producto sincronizado con ReadProduct: {product.nombreProducto}")
        else:
            print(f"⚠️ Error sincronizando con ReadProduct. Código: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error enviando solicitud a ReadProduct: {e}")
