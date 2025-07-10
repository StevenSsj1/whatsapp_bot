from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class WhatsAppMessage(Base):
    """Modelo para mensajes de WhatsApp"""
    __tablename__ = "whatsapp_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String, unique=True, index=True)
    phone_number = Column(String, nullable=False)
    message_type = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    media_url = Column(String, nullable=True)
    caption = Column(Text, nullable=True)
    status = Column(String, default="pending")
    sent_at = Column(DateTime, default=datetime.utcnow)
    delivered_at = Column(DateTime, nullable=True)
    read_at = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relación con usuario
    user = relationship("User", back_populates="messages")

class WhatsAppInstance(Base):
    """Modelo para instancias de WhatsApp"""
    __tablename__ = "whatsapp_instances"
    
    id = Column(Integer, primary_key=True, index=True)
    instance_name = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)
    is_connected = Column(Boolean, default=False)
    last_seen = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 