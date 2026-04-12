from pydantic import BaseModel, EmailStr
from typing import List, Optional

class DoctorCreate(BaseModel):
    nombre: str
    telefono: str
    correo: Optional[EmailStr] = None
    especialidades_ids: List[int]