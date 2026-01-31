import os

# Use /home for Azure App Service persistence
BASE_DIR = os.environ.get("HOME", os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR == "/":
    BASE_DIR = "/home/site/wwwroot"

DB_PATH = os.path.join(BASE_DIR, "clinic.db")

# Force SQLite - ignore Azure's auto-configured DATABASE_URL for PostgreSQL
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"

SQLALCHEMY_TRACK_MODIFICATIONS = False
