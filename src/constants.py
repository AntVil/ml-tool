import os

# database
DATABASE = "postgres"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "postgres"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"

# folders
SOURCE_FOLDER = os.path.dirname(__file__)
INTERFACE_FOLDER = os.path.join(SOURCE_FOLDER, "interface")
