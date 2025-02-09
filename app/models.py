from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombreProducto = Column(String(255), nullable=False)
    descripcion = Column(String(500))
    marca = Column(String(100), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    proveedor_id = Column(Integer, nullable=False)  # Referencia al proveedor
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
