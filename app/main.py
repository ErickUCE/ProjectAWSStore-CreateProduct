from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv
import os

load_dotenv()  # 🔥 Esto carga las variables de `.env`

# Verificar que se cargó correctamente
print("📌 PROVIDER_SERVICE_URL:", os.getenv("PROVIDER_SERVICE_URL"))

app = FastAPI()

# Incluir las rutas
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}
