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
        proveedor_nombre=nombre_proveedor  # ✅ Nuevo campo con el nombre del proveedor
        # No se incluye updated_at aquí, lo maneja automáticamente MySQL
    )
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    print(f"✅ Producto creado en CreateProduct: {db_product.nombreProducto}")

   # 🔄 **Sincronizar con ReadProduct y UpdateProduct**
    sync_with_microservices(db_product)

    return {
        "id": db_product.id,
        "nombreProducto": db_product.nombreProducto,
        "descripcion": db_product.descripcion,
        "marca": db_product.marca,
        "precio": float(db_product.precio),  # ✅ Convertir Decimal a float
        "proveedor_id": db_product.proveedor_id,
        "proveedor_nombre": db_product.proveedor_nombre
    }


def sync_update_product(product_data: dict, db: Session):
    """ 📌 Sincronizar la actualización del producto desde `UpdateProduct` """
    
    db_product = db.query(Product).filter(Product.id == product_data["id"]).first()
    if not db_product:
        print(f"⚠️ Producto con ID {product_data['id']} no encontrado en CreateProduct.")
        return {"error": "Producto no encontrado en CreateProduct"}

    # 🔄 Actualizar los datos del producto
    for key, value in product_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    
    print(f"✅ Producto sincronizado en CreateProduct: {db_product.nombreProducto}")
    return db_product

def sync_with_microservices(product):
    """ 🔄 Enviar producto a `ReadProduct` y `UpdateProduct` """
    
    print(f"🚀 Enviando producto a sincronización...")  # Verificación adicional

    services = [
        os.getenv("READ_PRODUCT_SERVICE_URL", "http://localhost:8002") + "/sync-create",  # ReadProduct
        os.getenv("UPDATE_PRODUCT_SERVICE_URL", "http://localhost:8003") + "/sync-create",  # UpdateProduct
         os.getenv("DELETE_PRODUCT_SERVICE_URL", "http://localhost:8004") + "/sync-create"  # DELETEProduct
    ]

    product_data = {
        "id": product.id,
        "nombreProducto": product.nombreProducto,
        "descripcion": product.descripcion,
        "marca": product.marca,
        "precio": float(product.precio),  # Convertir Decimal a float
        "proveedor_id": product.proveedor_id,
        "proveedor_nombre": product.proveedor_nombre,
    }

    for service in services:
        try:
            print(f"🚀 Enviando solicitud POST a {service}")  # Esto nos ayudará a ver si la solicitud está siendo enviada.
            response = requests.post(service, json=product_data)
            if response.status_code == 200:
                print(f"✅ Producto sincronizado con {service}: {product.nombreProducto}")
            else:
                print(f"⚠️ Error sincronizando con {service}. Código: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Error enviando solicitud a {service}: {e}")

