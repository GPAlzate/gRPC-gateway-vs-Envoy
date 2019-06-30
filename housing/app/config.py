import os

USER = os.getenv('POSTGRES_USER', 'postgres')
PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
HOST = os.getenv('POSTGRES_HOST', 'postgres')
PORT = os.getenv('POSTGRES_PORT', '5432')
DATABASE = os.getenv('POSTGRES_DB', 'postgres')
