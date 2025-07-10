from fastapi import HTTPException, status

class WhatsAppConnectionError(HTTPException):
    """Excepción para errores de conexión con WhatsApp"""
    def __init__(self, detail: str = "Error de conexión con WhatsApp"):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=detail
        )

class MessageSendError(HTTPException):
    """Excepción para errores al enviar mensajes"""
    def __init__(self, detail: str = "Error al enviar mensaje"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )

class InvalidPhoneNumberError(HTTPException):
    """Excepción para números de teléfono inválidos"""
    def __init__(self, detail: str = "Número de teléfono inválido"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )

class MessageTooLongError(HTTPException):
    """Excepción para mensajes demasiado largos"""
    def __init__(self, detail: str = "El mensaje es demasiado largo"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )

class MediaUploadError(HTTPException):
    """Excepción para errores al subir medios"""
    def __init__(self, detail: str = "Error al subir archivo multimedia"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        ) 