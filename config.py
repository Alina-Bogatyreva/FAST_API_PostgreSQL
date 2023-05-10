import os


if 'POSTGRES_DB' in os.environ:
    DB_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}" \
             f"@localhost:5432/{os.getenv('POSTGRES_DB')}"
else:
    DB_URL = f"postgresql://ilyas:admin123@localhost:5432/ilyas_db"

mode = "docker"
POSTGRES_HOST = "localhost" if mode == "local" else "192.168.99.100"
POSTGRES_DB = os.getenv("POSTGRES_DB") or "alina_db"
POSTGRES_USER = os.getenv("POSTGRES_USER") or "alina"
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") or "admin123"