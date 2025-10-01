import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

class Config:
    # -------------------
    # Melo API
    # -------------------
    MELO_API_KEY = os.getenv("MELO_API_KEY")
    MELO_BASE_URL = os.getenv("MELO_BASE_URL", "https://api.melo.io")

    # -------------------
    # DVF+ API
    # -------------------
    DVF_API_KEY = os.getenv("DVF_API_KEY")
    DVF_BASE_URL = os.getenv("DVF_BASE_URL", "https://geoservices.sogefi-sig.com/api/dvfplus/v1.0")

    # -------------------
    # Database
    # -------------------
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "real_estate")

    # -------------------
    # Pipeline
    # -------------------
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 100))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
