from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware  # ✅ Importar CORSMiddleware


load_dotenv()  # 🔥 Esto carga las variables de `.env`

# Verificar que se cargó correctamente
print("📌 xd PROVIDER_SERVICE_URL:", os.getenv("PROVIDER_SERVICE_URL"))

app = FastAPI()

# ✅ Configuración de CORS correcta para permitir el acceso desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Permitir todas las solicitudes (cámbialo luego a ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # ✅ Agregar "OPTIONS"
    allow_headers=["*"],  # ✅ Permitir todos los encabezados
)
# Incluir las rutas
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}

