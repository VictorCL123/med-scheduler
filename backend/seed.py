from sqlmodel import SQLModel, Session, select
from app.db.database import engine
from app.models.models import Rol, Especialidad, TipoDisponibilidad


def seed_data():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # 1. Llenar Roles
        roles_nombres = ["Paciente", "Doctor", "Recepcionista"]
        for nombre in roles_nombres:
            statement = select(Rol).where(Rol.rol == nombre)
            if not session.exec(statement).first():
                session.add(Rol(rol=nombre))
                print(f"Rol '{nombre}' creado.")

        # 2. Llenar Especialidades
        esp_nombres = ["Medicina general", "Cirugia", "Alergologo"]
        for nombre in esp_nombres:
            statement = select(Especialidad).where(Especialidad.especialidad == nombre)
            if not session.exec(statement).first():
                session.add(Especialidad(especialidad=nombre))
                print(f"Especialidad '{nombre}' creada.")

        # 3. Llenar Tipos de Disponibilidad
        tipos_disp = ["Semanal", "Quincenal", "Mensual", "Bloqueado"]
        for nombre in tipos_disp:
            statement = select(TipoDisponibilidad).where(
                TipoDisponibilidad.disponibilidad == nombre
            )
            if not session.exec(statement).first():
                session.add(TipoDisponibilidad(disponibilidad=nombre))
                print(f"Tipo de disponibilidad '{nombre}' creado.")

        session.commit()
        print("--- Proceso de seeding completado con éxito ---")


if __name__ == "__main__":
    seed_data()
