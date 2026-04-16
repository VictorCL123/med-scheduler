from app.db.database import engine
from app.models.models import User
from sqlmodel import Session, select


def test_crear_paciente_y_verificar_en_db(client):
    payload = {
        "nombre": "Juan Pérez",
        "correo": "juan@test.com",
        "telefono": "1234567890",
        "direccion": "Calle 123",
        "fecha_nacimiento": "1990-01-01",
    }

    # 1. Ejecutamos la acción a través de la API
    response = client.post("/api/v1/pacientes/registrar", json=payload)
    print(response.json())
    assert response.status_code == 201
    nuevo_id = response.json()["id"]

    # 2. CONSULTA DIRECTA A LA BASE DE DATOS
    with Session(engine) as session:
        # Buscamos el registro que acabamos de crear
        db_user = session.exec(select(User).where(User.id_user == nuevo_id)).first()

        # Validaciones extra
        assert db_user is not None
        assert db_user.nombre == "Juan Pérez"
        assert db_user.correo == "juan@test.com"
