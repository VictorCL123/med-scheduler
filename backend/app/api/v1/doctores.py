from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import User, DoctorEspecialidad, Rol
from app.schemas.doctor import DoctorCreate

router = APIRouter()

@router.post("/registrar", status_code=201)
def registrar_doctor(datos: DoctorCreate, session: Session = Depends(get_session)):
    # Obtener el ID del rol 'Doctor' dinámicamente
    rol_doctor = session.exec(select(Rol).where(Rol.rol == "Doctor")).first()
    if not rol_doctor:
        raise HTTPException(status_code=500, detail="Rol 'Doctor' no configurado. Ejecute el seed.")

    # Crear el nuevo Usuario
    nuevo_doctor = User(
        nombre=datos.nombre,
        correo=datos.correo,
        telefono=datos.telefono,
        id_rol=rol_doctor.id_rol
    )
    session.add(nuevo_doctor)
    session.commit()
    session.refresh(nuevo_doctor)

    # Asignar Especialidades
    for esp_id in datos.especialidades_ids:
        relacion = DoctorEspecialidad(id_doctor=nuevo_doctor.id_user, id_especialidad=esp_id)
        session.add(relacion)
    
    session.commit()
    
    return {"message": "Doctor registrado exitosamente", "id": nuevo_doctor.id_user}

@router.get("/", response_model=list[User])
def listar_doctores(session: Session = Depends(get_session)):
    # Filtramos solo los usuarios que tienen el rol de Doctor
    rol_doctor = session.exec(select(Rol).where(Rol.rol == "Doctor")).first()
    statement = select(User).where(User.id_rol == rol_doctor.id_rol)
    return session.exec(statement).all()