from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware  # ✅ Importar CORSMiddleware


load_dotenv()  # 🔥 Esto carga las variables de `.env`

# Verificar que se cargó correctamente
print("📌 PROVIDER_SERVICE_URL:", os.getenv("PROVIDER_SERVICE_URL"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir las rutas
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}
