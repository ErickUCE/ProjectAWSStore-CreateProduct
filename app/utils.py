import os
import requests

PROVIDER_SERVICE_URL = os.getenv("PROVIDER_SERVICE_URL", "http://localhost:5003")

def validar_proveedor(proveedor_id):
    """Verifica si el proveedor existe en ReadProvider antes de agregar un producto."""
    try:
        response = requests.get(f"{PROVIDER_SERVICE_URL}/providers/{proveedor_id}", timeout=5)
        response.raise_for_status()  # 🔥 Lanza un error si la respuesta no es 200
    except requests.exceptions.RequestException as e:
        raise ValueError(f"❌ Error conectando con ReadProvider: {e}")

    proveedor = response.json()
    if not proveedor:
        raise ValueError("⚠️ El proveedor no existe.")
    
    return proveedor
