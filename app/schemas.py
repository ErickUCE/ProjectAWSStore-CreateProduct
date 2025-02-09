from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    nombreProducto: str = Field(..., example="Laptop Dell")
    descripcion: Optional[str] = Field(None, example="Laptop Core i7 con 16GB RAM")
    marca: str = Field(..., example="Dell")
    precio: float = Field(..., example=899.99)
    proveedor_id: int = Field(..., example=1)
