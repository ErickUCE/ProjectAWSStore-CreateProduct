import requests
import os

PROVIDER_SERVICE_URL = os.getenv("PROVIDER_SERVICE_URL")

def obtener_nombre_proveedor(proveedor_id):
    """Consulta el nombre del proveedor usando su ID en ReadProvider."""
    try:
        response = requests.get(f"{PROVIDER_SERVICE_URL}/providers/{proveedor_id}")
        response.raise_for_status()
        data = response.json()
        return data.get("name")  # Obtiene el nombre del proveedor
    except requests.exceptions.RequestException as e:
        raise ValueError(f"❌ Error conectando con ReadProvider: {e}")

def validar_proveedor(proveedor_id):
    """Valida si el proveedor existe y retorna su nombre."""
    nombre_proveedor = obtener_nombre_proveedor(proveedor_id)
    if not nombre_proveedor:
        raise ValueError(f"❌ Proveedor con ID {proveedor_id} no encontrado.")
    return nombre_proveedor
