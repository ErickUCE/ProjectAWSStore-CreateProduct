from fastapi import FastAPI, Response
from app.routes import router
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib.parse

# 🔥 Cargar variables de entorno
load_dotenv()

# 📌 Variables de entorno para la base de datos
DB_USER = os.getenv("DB_USER", "default_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_password")
DB_PASSWORD = urllib.parse.quote_plus(DB_PASSWORD)  # ✅ Codificar contraseña
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "mydatabase")

# ✅ Construir la URL de conexión a MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 🔥 Crear motor de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Verificar que se cargaron correctamente las variables de entorno
print("📌 PROVIDER_SERVICE_URL:", os.getenv("PROVIDER_SERVICE_URL"))

# ✅ Inicializar la aplicación FastAPI
app = FastAPI()

# ✅ Configurar CORS correctamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Permitir todos los métodos
    allow_headers=["*"],  # ✅ Permitir todos los encabezados
)

@app.options("/{full_path:path}")
async def preflight_request(full_path: str, response: Response):
    """
    ✅ Endpoint para manejar OPTIONS y evitar el error 405
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# ✅ Incluir las rutas de la API
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}

# ✅ Iniciar el servidor solo si se ejecuta este script directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

