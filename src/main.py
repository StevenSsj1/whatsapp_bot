from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .config import settings
from .database import engine, Base
from .whatsapp.router import router as whatsapp_router

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manejar eventos del ciclo de vida de la aplicación"""
    # Startup
    print("🚀 Iniciando aplicación WhatsApp Bot...")
    yield
    # Shutdown
    print("👋 Cerrando aplicación...")

app = FastAPI(
    title="WhatsApp Bot API",
    description="API para integración con WhatsApp usando Evolution API",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(whatsapp_router)

@app.get("/")
async def root():
    """Endpoint raíz"""
    return {
        "message": "¡Bienvenido a WhatsApp Bot API!",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Endpoint de verificación de salud"""
    return {"status": "healthy"} 

