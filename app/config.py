import os
from dotenv import load_dotenv

# Cargar variables de entorno desde `.env`
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
PROVIDER_SERVICE_URL = os.getenv("PROVIDER_SERVICE_URL")
READ_PRODUCT_SERVICE="http://44.195.73.5:8007"
UPDATE_PRODUCT_SERVICE="http://54.165.250.5:8006"
DELETE_PRODUCT_SERVICE="http://52.44.127.200:8005"