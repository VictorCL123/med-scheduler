# 🩺 Med-Scheduler

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLModel](https://img.shields.io/badge/SQLModel-SQLAlchemy-red?style=for-the-badge)](https://sqlmodel.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

**Med-Scheduler** es una solución de backend de alto rendimiento para la gestión de citas médicas. Diseñada bajo principios de **Clean Architecture**, esta API resuelve el desafío de la disponibilidad dinámica y la gestión de catálogos especializados para el sector salud.

---

## 🏗️ Arquitectura y Diseño

El proyecto está estructurado para facilitar el mantenimiento y las pruebas automatizadas:

* **Modularidad:** Separación estricta entre modelos de persistencia (`models/`) y esquemas de validación de datos (`schemas/`).
* **Gestión de Catálogos:** Implementación de sistemas de seeding para roles, especialidades y tipos de jornada.
* **Motor de Disponibilidad:** Lógica avanzada que calcula slots de tiempo libres mediante la intersección de horarios laborales y citas agendadas.

---

## 🛠️ Stack Tecnológico

* **Core:** FastAPI para una ejecución asíncrona y eficiente.
* **Data:** SQLModel (unificación de SQLAlchemy + Pydantic) para una manipulación de datos con tipado fuerte.
* **Database:** PostgreSQL (vía Supabase) con soporte para integridad referencial compleja.
* **Configuración:** Pydantic-Settings para la gestión segura de variables de entorno.

---

## 🚦 Instalación y Configuración

### 1. Preparación del Entorno
```bash
# Clonar el repositorio
git clone [https://github.com/tu-usuario/med-scheduler.git](https://github.com/tu-usuario/med-scheduler.git)
cd med-scheduler/backend

# Crear y activar venv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```
### 2. Variables de entorno
DATABASE_URL=postgresql://[usuario]:[password]@host:[port]/postgres

### 3. Inicialización
Ejecuta el script de semilla para cargar los catálogos base:
```bash
python seed.py
```

## 🔌 API Documentation (Highlights)

| Recurso | Método | Endpoint | Acción |
| :--- | :--- | :--- | :--- |
| 👨‍⚕️ **Doctores** | `POST` | `/api/v1/doctores/registrar` | Alta de médicos con especialidades vinculadas. |
| 👤 **Pacientes** | `POST` | `/api/v1/pacientes/registrar` | Registro rápido de usuarios pacientes. |
| 📝 **Citas** | `POST` | `/api/v1/citas/agendar` | Reserva de cita con validación de conflictos. |
| 📋 **Catálogos** | `GET` | `/api/v1/catalogos/roles` | Listado de roles del sistema. |