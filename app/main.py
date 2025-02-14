from fastapi import FastAPI, Response
from app.routes import router
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware  # ✅ Importar CORSMiddleware
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


load_dotenv()  # 🔥 Esto carga las variables de `.env`

# Verificar que se cargó correctamente
print("📌 xd PROVIDER_SERVICE_URL:", os.getenv("PROVIDER_SERVICE_URL"))

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
# Incluir las rutas
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}

