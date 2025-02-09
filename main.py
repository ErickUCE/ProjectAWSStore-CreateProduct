from fastapi import FastAPI
from dotenv import load_dotenv
import os

# 📌 Cargar variables del `.env`
load_dotenv()

app = FastAPI()

# 📌 Mostrar la URL del servicio de proveedores en la terminal
print(f"🔗 PROVIDER_SERVICE_URL: {os.getenv('PROVIDER_SERVICE_URL')}")

# Ejecutar con:
# uvicorn main:app --host 0.0.0.0 --port 8081 --reload
