from datetime import date, time, datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# --- Tablas de Catálogo ---
class Rol(SQLModel, table=True):
    id_rol: Optional[int] = Field(default=None, primary_key=True)
    rol: str

class Especialidad(SQLModel, table=True):
    id_especialidad: Optional[int] = Field(default=None, primary_key=True)
    especialidad: str

class TipoDisponibilidad(SQLModel, table=True):
    id_tipo_disponibilidad: Optional[int] = Field(default=None, primary_key=True)
    disponibilidad: str  # Ej: Recurrente, Única, Bloqueo

# --- Tablas de Relación ---
class DoctorEspecialidad(SQLModel, table=True):
    id_doctor: int = Field(foreign_key="user.id_user", primary_key=True)
    id_especialidad: int = Field(foreign_key="especialidad.id_especialidad", primary_key=True)

# --- Entidades Principales ---
class User(SQLModel, table=True):
    id_user: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    telefono: str
    correo: Optional[str] = None
    direccion: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    id_rol: int = Field(foreign_key="rol.id_rol")

class Disponibilidad(SQLModel, table=True):
    id_disponibilidad: Optional[int] = Field(default=None, primary_key=True)
    id_doctor: int = Field(foreign_key="user.id_user")
    id_tipo_disponibilidad: int = Field(foreign_key="tipodisponibilidad.id_tipo_disponibilidad")
    dia_semana: Optional[int] = None # 0-6
    fecha_unica: Optional[date] = None
    fecha_inicio: Optional[date] = None
    fecha_final: Optional[date] = None
    hora_inicio: time
    hora_final: time
    turnos: Optional[str] = None # Mañana/Tarde/Noche

class Cita(SQLModel, table=True):
    id_cita: Optional[int] = Field(default=None, primary_key=True)
    id_paciente: int = Field(foreign_key="user.id_user")
    id_doctor: int = Field(foreign_key="user.id_user")
    id_especialidad: int = Field(foreign_key="especialidad.id_especialidad")
    motivo: str
    fecha_inicio: datetime
    fecha_final: Optional[datetime] = None
    turno: Optional[str] = None