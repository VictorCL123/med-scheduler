from pydantic import BaseModel, EmailStr
from typing import Optional

class PacienteCreate(BaseModel):
    nombre: str
    telefono: str
    correo: Optional[EmailStr] = None
    direccion: Optional[str] = None
    fecha_nacimiento: Optional[str] = None  # Formato 'YYYY-MM-DD'