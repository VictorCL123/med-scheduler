import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Retorna un cliente de pruebas para la API"""
    with TestClient(app) as c:
        yield c
