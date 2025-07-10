from typing import TypeVar, Generic, List, Optional
from pydantic import BaseModel
from fastapi import Query

T = TypeVar('T')

class PageInfo(BaseModel):
    """Información de paginación"""
    page: int
    size: int
    total: int
    pages: int
    has_next: bool
    has_prev: bool

class PaginatedResponse(BaseModel, Generic[T]):
    """Respuesta paginada"""
    items: List[T]
    page_info: PageInfo

def get_pagination_params(
    page: int = Query(1, ge=1, description="Número de página"),
    size: int = Query(10, ge=1, le=100, description="Tamaño de página")
) -> tuple[int, int]:
    """Obtener parámetros de paginación"""
    return page, size

def create_page_info(page: int, size: int, total: int) -> PageInfo:
    """Crear información de página"""
    pages = (total + size - 1) // size
    return PageInfo(
        page=page,
        size=size,
        total=total,
        pages=pages,
        has_next=page < pages,
        has_prev=page > 1
    ) 