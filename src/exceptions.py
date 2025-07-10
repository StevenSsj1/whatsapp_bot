from fastapi import HTTPException, status

class AppException(HTTPException):
    """Excepción base de la aplicación"""
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class DatabaseError(AppException):
    """Excepción para errores de base de datos"""
    def __init__(self, detail: str = "Error de base de datos"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class ValidationError(AppException):
    """Excepción para errores de validación"""
    def __init__(self, detail: str = "Error de validación"):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)

class NotFoundError(AppException):
    """Excepción para recursos no encontrados"""
    def __init__(self, detail: str = "Recurso no encontrado"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class ConflictError(AppException):
    """Excepción para conflictos de recursos"""
    def __init__(self, detail: str = "Conflicto de recursos"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail) 