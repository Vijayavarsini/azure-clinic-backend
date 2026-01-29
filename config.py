# config.py

import os

DB_USERNAME = "clinicadmin"
DB_PASSWORD = "1234Viju*"
DB_HOST = "pg-clinic-db-varsini.postgres.database.azure.com"
DB_NAME = "clinicdb"

SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://clinicadmin:1234Viju%2A"
    "@pg-clinic-db-varsini.postgres.database.azure.com:5432/clinicdb"
    "?sslmode=require"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False