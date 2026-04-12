from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import User, Rol
from app.schemas.paciente import PacienteCreate

router = APIRouter()

@router.post("/registrar", status_code=201)
def registrar_paciente(datos: PacienteCreate, session: Session = Depends(get_session)):
    # Obtener el ID del rol 'Paciente' dinámicamente
    rol_paciente = session.exec(select(Rol).where(Rol.rol == "Paciente")).first()
    if not rol_paciente:
        raise HTTPException(status_code=500, detail="El rol 'Paciente' no existe en los catálogos.")

    # Crear el nuevo Usuario con rol de Paciente
    nuevo_paciente = User(
        nombre=datos.nombre,
        telefono=datos.telefono,
        correo=datos.correo,
        direccion=datos.direccion,
        fecha_nacimiento=datos.fecha_nacimiento,
        id_rol=rol_paciente.id_rol
    )
    
    session.add(nuevo_paciente)
    session.commit()
    session.refresh(nuevo_paciente)
    
    return {"message": "Paciente registrado con éxito", "id": nuevo_paciente.id_user}

@router.get("/", response_model=list[User])
def listar_pacientes(session: Session = Depends(get_session)):
    # Obtenemos el ID del rol para filtrar
    rol_paciente = session.exec(select(Rol).where(Rol.rol == "Paciente")).first()
    statement = select(User).where(User.id_rol == rol_paciente.id_rol)
    return session.exec(statement).all()