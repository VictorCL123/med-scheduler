from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select, and_


from app.db.database import engine, create_db_and_tables, get_session
from app.models.models import User, Cita, Disponibilidad, TipoDisponibilidad
from app.api.v1.catalogos import router as catalogos_router
from app.api.v1.doctores import router as doctores_router
from app.api.v1.pacientes import router as pacientes_router
from app.api.v1.citas import router as citas_router

from datetime import date

# 1. Definimos el gestor de ciclo de vida
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lógica de Inicio (Startup)
    # Aquí puedes crear tablas, conectar a Redis, etc.
    create_db_and_tables()
    
    yield  # Aquí es donde la aplicación "corre"
    
    # Lógica de Cierre (Shutdown)
    # Aquí cerrarías conexiones a DB o pools si fuera necesario
    # engine.dispose() 

# 2. Pasamos el lifespan a la instancia de FastAPI
app = FastAPI(title="Agendador API", lifespan=lifespan)

# --- Endpoints ---
app.include_router(
    catalogos_router, 
    prefix="/api/v1/catalogos", 
    tags=["Catálogos"]
)

app.include_router(
    doctores_router, 
    prefix="/api/v1/doctores", 
    tags=["Doctores"]
)

app.include_router(
    pacientes_router, 
    prefix="/api/v1/pacientes", 
    tags=["Pacientes"]
)

app.include_router(
    citas_router,
    prefix="/api/v1/citas",
    tags=["Citas"]
)
