from typing import List, Optional
from pydantic import BaseModel

class AtletaBase(BaseModel):
    nome: str
    centro_treinamento: Optional[str] = None
    categoria: Optional[str] = None

class AtletaCreate(AtletaBase):
    cpf: str

class Atleta(AtletaBase):
    id: int
    cpf: str

    class Config:
        orm_mode = True

class Page(BaseModel):
    items: List[Atleta]
    total: int
    page: int
    size: int
    pages: int
