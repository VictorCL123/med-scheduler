import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.pool import QueuePool

# Cargamos el archivo .env
load_dotenv()

# Obtenemos la URL de la base de datos
DATABASE_URL = os.getenv("SUPABASE_URL")

if not DATABASE_URL:
    raise ValueError("No se encontró SUPABASE_URL en el archivo .env")

# Configuración del Engine para Producción
# - echo=False en producción para evitar logs masivos de SQL.
# - pool_size y max_overflow ayudan a gestionar conexiones concurrentes en Supabase.
engine = create_engine(
    DATABASE_URL,
    echo=False,  
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True  # Verifica si la conexión sigue viva (vital para Supabase)
)

def create_db_and_tables():
    """
    Crea las tablas en Supabase. 
    Nota: En un entorno profesional, preferirás usar Alembic para migraciones.
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Dependency Injection para FastAPI. 
    Asegura que la sesión se cierre automáticamente después de cada request.
    """
    with Session(engine) as session:
        yield session