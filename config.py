import os

BASE_DIR = "/home/site/wwwroot"
DB_PATH = os.path.join(BASE_DIR, "clinic.db")

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    f"sqlite:///{DB_PATH}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
