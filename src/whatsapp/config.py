from pydantic_settings import BaseSettings

class WhatsAppSettings(BaseSettings):
    """Configuraciones para el módulo de WhatsApp"""
    
    # Evolution API settings
    EVOLUTION_API_URL: str = "http://localhost:8080"
    API_KEY: str = "your-api-key-here"
    INSTANCE_NAME: str = "default"
    
    # Webhook settings
    WEBHOOK_URL: str = "http://localhost:8000/whatsapp/webhook"
    WEBHOOK_ENABLED: bool = True
    
    # Message settings
    MAX_MESSAGE_LENGTH: int = 4096
    MAX_MEDIA_SIZE_MB: int = 16
    
    # Retry settings
    MAX_RETRY_ATTEMPTS: int = 3
    RETRY_DELAY_SECONDS: int = 5
    
    class Config:
        env_file = ".env"
        env_prefix = "WHATSAPP_" 