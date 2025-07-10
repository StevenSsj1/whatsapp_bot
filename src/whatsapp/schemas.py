from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class MessageType(str, Enum):
    """Tipos de mensaje de WhatsApp"""
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    DOCUMENT = "document"
    LOCATION = "location"
    CONTACT = "contact"

class MessageStatus(str, Enum):
    """Estados de mensaje"""
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"
    FAILED = "failed"
    PENDING = "pending"

class MessageCreate(BaseModel):
    """Esquema para crear mensaje"""
    phone_number: str
    message_type: MessageType
    content: str
    media_url: Optional[str] = None
    caption: Optional[str] = None

class MessageResponse(BaseModel):
    """Esquema para respuesta de mensaje"""
    id: str
    phone_number: str
    message_type: MessageType
    content: str
    status: MessageStatus
    sent_at: datetime
    delivered_at: Optional[datetime] = None
    read_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class WebhookPayload(BaseModel):
    """Esquema para payload de webhook"""
    event: str
    data: Dict[str, Any]
    timestamp: datetime

class ConnectionStatus(BaseModel):
    """Esquema para estado de conexión"""
    is_connected: bool
    instance_name: Optional[str] = None
    phone_number: Optional[str] = None
    last_seen: Optional[datetime] = None 