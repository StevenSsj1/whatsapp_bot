# WhatsApp Bot API

API para integración con WhatsApp usando Evolution API y FastAPI.

## 🚀 Características

- **Autenticación JWT**: Sistema de autenticación seguro
- **Integración con WhatsApp**: Envío y recepción de mensajes
- **Base de datos SQLite/PostgreSQL**: Almacenamiento de datos
- **Documentación automática**: Swagger UI y ReDoc
- **Estructura modular**: Organización clara del código
- **Testing**: Tests unitarios y de integración
- **Docker**: Containerización para despliegue

## 📁 Estructura del Proyecto

```
fastapi-project/
├── alembic/                    # Migraciones de base de datos
├── src/
│   ├── whatsapp/              # Módulo de WhatsApp
│   │   ├── router.py          # Endpoints de WhatsApp
│   │   ├── schemas.py         # Modelos Pydantic
│   │   ├── models.py          # Modelos de BD
│   │   ├── service.py         # Lógica de negocio
│   │   ├── config.py          # Configuraciones
│   │   └── exceptions.py      # Excepciones
│   ├── config.py              # Configuraciones globales
│   ├── database.py            # Configuración de BD
│   ├── exceptions.py          # Excepciones globales
│   ├── pagination.py          # Utilidades de paginación
│   └── main.py                # Aplicación principal
├── tests/                     # Tests
│   ├── whatsapp/
├── requirements/              # Dependencias
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env                       # Variables de entorno
├── .gitignore
├── alembic.ini               # Configuración Alembic
└── README.md
```

## 🛠️ Instalación

### Prerrequisitos

- Python 3.8+
- Evolution API configurada
- Base de datos (SQLite/PostgreSQL)

### Instalación

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd whatsapp-bot
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements/dev.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Configurar base de datos**
```bash
# Crear migraciones
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

6. **Ejecutar la aplicación**
```bash
uvicorn src.main:app --reload
```

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` con las siguientes variables:

```env
# Configuraciones de la aplicación
APP_NAME=WhatsApp Bot API
DEBUG=true
VERSION=1.0.0

# Base de datos
DATABASE_URL=sqlite:///./whatsapp_bot.db

# Evolution API
EVOLUTION_API_URL=http://localhost:8080
EVOLUTION_API_KEY=your-evolution-api-key
EVOLUTION_INSTANCE_NAME=default

# WhatsApp settings
WHATSAPP_EVOLUTION_API_URL=http://localhost:8080
WHATSAPP_API_KEY=your-api-key-here
WHATSAPP_INSTANCE_NAME=default
```

## 🚀 Despliegue

### Desarrollo

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```
