# Usa la imagen oficial de Python 3.11
FROM python:3.11

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre la aplicación
EXPOSE 8000

# Comando para ejecutar FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
