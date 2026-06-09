from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    descricao: Optional[str] = Field(None, max_length=255)
    preco: float = Field(..., gt=0)
    quantidade_estoque: int = Field(..., ge=0)
    estoque_minimo: int = Field(5, ge=0)

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    descricao: Optional[str] = Field(None, max_length=255)
    preco: Optional[float] = Field(None, gt=0)
    quantidade_estoque: Optional[int] = Field(None, ge=0)
    estoque_minimo: Optional[int] = Field(None, ge=0)

class ProdutoResponse(ProdutoBase):
    id: int
    criado_em: datetime
    atualizado_em: Optional[datetime]

    class Config:
        from_attributes = True