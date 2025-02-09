import os
from dotenv import load_dotenv

# Cargar variables de entorno desde `.env`
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
PROVIDER_SERVICE_URL = os.getenv("PROVIDER_SERVICE_URL")
