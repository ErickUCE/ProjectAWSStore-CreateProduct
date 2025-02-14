from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()

# 🔥 Permitir cualquier origen, credenciales, métodos y encabezados
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Permitir todos los dominios (cámbialo en producción)
    allow_credentials=True,
    allow_methods=["*"],  # 🔥 Permitir todos los métodos
    allow_headers=["*"],  # 🔥 Permitir todos los headers
)

# ✅ Asegurar que FastAPI tenga un endpoint de prueba
@app.get("/")
def home():
    return {"message": "API de Productos en FastAPI funcionando correctamente"}

# ✅ Incluir las rutas del backend
app.include_router(router)
