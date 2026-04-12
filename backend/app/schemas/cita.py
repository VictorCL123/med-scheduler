from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CitaCreate(BaseModel):
    id_paciente: int
    id_doctor: int
    id_especialidad: int
    fecha_inicio: datetime
    fecha_final: Optional[datetime] = None
    motivo: Optional[str]