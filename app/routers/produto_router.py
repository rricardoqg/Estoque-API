from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.produto_controller import produto_controller
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from typing import List

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.post("/", response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return produto_controller.criar(db, produto)

@router.get("/criticos", response_model=List[ProdutoResponse])
def listar_criticos(db: Session = Depends(get_db)):
    return produto_controller.listar_criticos(db)

@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return produto_controller.listar(db)

@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    return produto_controller.buscar(db, produto_id)

@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoUpdate, db: Session = Depends(get_db)):
    return produto_controller.atualizar(db, produto_id, dados)

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    return produto_controller.deletar(db, produto_id)