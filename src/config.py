from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Configuraciones globales de la aplicación"""
    
    # Configuraciones de la aplicación
    APP_NAME: str = "WhatsApp Bot API"
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    
    # Configuraciones de base de datos
    DATABASE_URL: str = "sqlite:///./whatsapp_bot.db"
    
    
    # Configuraciones de CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000"
    ]
    
    # Configuraciones de logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    # Configuraciones de Evolution API
    EVOLUTION_API_URL: str = "http://localhost:8080"
    EVOLUTION_API_KEY: str = "your-evolution-api-key"
    EVOLUTION_INSTANCE_NAME: str = "default"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Instancia global de configuraciones
settings = Settings() 