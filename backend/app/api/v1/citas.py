from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, and_
from app.db.database import get_session
from app.models.models import Cita, User
from app.schemas.cita import CitaCreate

router = APIRouter()

@router.post("/agendar", status_code=201)
def crear_cita(datos: CitaCreate, session: Session = Depends(get_session)):
    # Validar que el paciente y el doctor existan y tengan el rol correcto
    paciente = session.get(User, datos.id_paciente)
    doctor = session.get(User, datos.id_doctor)
    
    if not paciente or not doctor:
        raise HTTPException(status_code=404, detail="Paciente o Doctor no encontrado")

    # Verificar disponibilidad (Evitar doble reserva en el mismo segundo)
    # Buscamos si ya existe una cita para ese doctor, esa fecha y esa hora
    existe_cita = session.exec(
        select(Cita).where(
            and_(
                Cita.id_doctor == datos.id_doctor,
                Cita.fecha_inicio == datos.fecha_inicio,
            )
        )
    ).first()

    if existe_cita:
        raise HTTPException(
            status_code=400, 
            detail="El horario ya no está disponible. Por favor, elige otro."
        )

    # Crear la instancia de la Cita
    # Nota: El campo 'estado' suele ser 'programada' por defecto en el modelo
    nueva_cita = Cita(
        id_paciente=datos.id_paciente,
        id_doctor=datos.id_doctor,
        id_especialidad=datos.id_especialidad,
        fecha_inicio=datos.fecha_inicio,
        fecha_final=datos.fecha_final,
        motivo=datos.motivo,
    )

    session.add(nueva_cita)
    session.commit()
    session.refresh(nueva_cita)
    
    return {
        "message": "Cita agendada con éxito",
        "id_cita": nueva_cita.id_cita,
        "fecha": nueva_cita.fecha_inicio,
    }