from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombreProducto = Column(String(255), nullable=False)
    descripcion = Column(Text)
    marca = Column(String(100), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    proveedor_id = Column(Integer, nullable=False)  # Sigue almacenando el ID
    proveedor_nombre = Column(String(255), nullable=False)  # 🔥 Nuevo campo
    