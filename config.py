import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN", "tocken")

DB_CONFIG = {
    "database": os.environ.get("DB_NAME", 'wordlydb'),
    "user": os.environ.get("DB_USER", 'admin'),
    "password": os.environ.get("DB_PASSWORD", 'admin'),
    "host": os.environ.get("DB_HOST", 'localhost'),
    "port": os.environ.get("DB_PORT", 5432),
}
