from fastapi import APIRouter, Depends, HTTPException
from typing import List

from .schemas import MessageCreate, MessageResponse, WebhookPayload
from .service import WhatsAppService

router = APIRouter(prefix="/whatsapp", tags=["whatsapp"])

@router.post("/send-message")
async def send_message(
    message: MessageCreate,
):
    """Enviar mensaje de WhatsApp"""
    pass

@router.get("/messages", response_model=List[MessageResponse])
async def get_messages(
):
    """Obtener historial de mensajes"""
    pass

@router.post("/webhook")
async def webhook_handler(payload: WebhookPayload):
    """Manejar webhooks de WhatsApp"""
    pass

@router.get("/status")
async def get_connection_status():
    """Obtener estado de conexión con WhatsApp"""
    pass 