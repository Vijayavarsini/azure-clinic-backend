import os

DB_USERNAME = "clinicadmin"
DB_PASSWORD = "vijay@123"
DB_HOST = "pg-clinic-db-varsini.postgres.database.azure.com"
DB_NAME = "clinicdb"

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}"
    f"@{DB_HOST}:5432/{DB_NAME}"
    "?sslmode=require"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False