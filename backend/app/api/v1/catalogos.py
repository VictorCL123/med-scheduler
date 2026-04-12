from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import Rol, Especialidad, TipoDisponibilidad
from typing import List

router = APIRouter()

@router.get("/roles", response_model=List[Rol])
def obtener_roles(session: Session = Depends(get_session)):
    return session.exec(select(Rol)).all()

@router.get("/especialidades", response_model=List[Especialidad])
def obtener_especialidades(session: Session = Depends(get_session)):
    return session.exec(select(Especialidad)).all()

@router.get("/tipos-disponibilidad", response_model=List[TipoDisponibilidad])
def obtener_tipos_disponibilidad(session: Session = Depends(get_session)):
    return session.exec(select(TipoDisponibilidad)).all()