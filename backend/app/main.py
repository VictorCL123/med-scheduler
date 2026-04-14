from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import create_db_and_tables
from app.api.v1.catalogos import router as catalogos_router
from app.api.v1.doctores import router as doctores_router
from app.api.v1.pacientes import router as pacientes_router
from app.api.v1.citas import router as citas_router


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

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite a Vite acceder
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Permite todos los headers
)

# --- Endpoints ---
app.include_router(catalogos_router, prefix="/api/v1/catalogos", tags=["Catálogos"])

app.include_router(doctores_router, prefix="/api/v1/doctores", tags=["Doctores"])

app.include_router(pacientes_router, prefix="/api/v1/pacientes", tags=["Pacientes"])

app.include_router(citas_router, prefix="/api/v1/citas", tags=["Citas"])
