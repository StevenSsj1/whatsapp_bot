import httpx
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

from .models import WhatsAppMessage, WhatsAppInstance
from .schemas import MessageCreate, MessageResponse, ConnectionStatus
from .config import WhatsAppSettings
from .exceptions import WhatsAppConnectionError, MessageSendError

class WhatsAppService:
    """Servicio para manejar la lógica de WhatsApp"""
    
    def __init__(self):
        self.settings = WhatsAppSettings()
        self.base_url = f"{self.settings.EVOLUTION_API_URL}/instance"
    
    async def send_message(self, db: Session, message: MessageCreate, user_id: int) -> WhatsAppMessage:
        """Enviar mensaje de WhatsApp"""
        try:
            # Crear mensaje en base de datos
            db_message = WhatsAppMessage(
                phone_number=message.phone_number,
                message_type=message.message_type.value,
                content=message.content,
                media_url=message.media_url,
                caption=message.caption,
                user_id=user_id
            )
            db.add(db_message)
            db.commit()
            db.refresh(db_message)
            
            # Enviar mensaje a Evolution API
            async with httpx.AsyncClient() as client:
                payload = {
                    "number": message.phone_number,
                    "text": message.content
                }
                
                response = await client.post(
                    f"{self.base_url}/{self.settings.INSTANCE_NAME}/sendText",
                    json=payload,
                    headers={"apikey": self.settings.API_KEY}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    db_message.message_id = data.get("key", {}).get("id")
                    db_message.status = "sent"
                    db_message.sent_at = datetime.utcnow()
                else:
                    db_message.status = "failed"
                
                db.commit()
                return db_message
                
        except Exception as e:
            raise MessageSendError(f"Error al enviar mensaje: {str(e)}")
    
    async def get_messages(self, db: Session, user_id: int) -> List[WhatsAppMessage]:
        """Obtener mensajes del usuario"""
        return db.query(WhatsAppMessage).filter(WhatsAppMessage.user_id == user_id).all()
    
    async def get_connection_status(self, db: Session) -> ConnectionStatus:
        """Obtener estado de conexión"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/{self.settings.INSTANCE_NAME}/connectionState",
                    headers={"apikey": self.settings.API_KEY}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return ConnectionStatus(
                        is_connected=data.get("state") == "open",
                        instance_name=self.settings.INSTANCE_NAME,
                        phone_number=data.get("phone"),
                        last_seen=datetime.utcnow()
                    )
                else:
                    return ConnectionStatus(is_connected=False)
                    
        except Exception:
            return ConnectionStatus(is_connected=False)
    
    async def handle_webhook(self, db: Session, payload: dict):
        """Manejar webhook de WhatsApp"""
        # Implementar lógica de webhook
        pass 