from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware  # ✅ Importar CORSMiddleware


load_dotenv()  # 🔥 Esto carga las variables de `.env`

# Verificar que se cargó correctamente
print("📌 xd PROVIDER_SERVICE_URL:", os.getenv("PROVIDER_SERVICE_URL"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Permitir todas las conexiones (solo para pruebas)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}

# 🔥 Endpoint explícito para manejar `OPTIONS` y evitar el error 405
@app.options("/{full_path:path}")
async def preflight(full_path: str):
    return {"message": "Preflight request handled"}