from sqlalchemy.orm import Session
from app.repositories.produto_repository import produto_repository
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate
from app.models.produto import Produto
from fastapi import HTTPException
from typing import Optional

class ProdutoService:

    def criar_produto(self, db: Session, produto: ProdutoCreate) -> Produto:
        if produto.preco <= 0:
            raise HTTPException(
                status_code=400,
                detail="Preço deve ser maior que zero"
            )
        if produto.quantidade_estoque < 0:
            raise HTTPException(
                status_code=400,
                detail="Quantidade em estoque não pode ser negativa"
            )
        return produto_repository.criar(db, produto)

    def buscar_produto(self, db: Session, produto_id: int) -> Produto:
        produto = produto_repository.buscar_por_id(db, produto_id)
        if not produto:
            raise HTTPException(
                status_code=404,
                detail=f"Produto {produto_id} não encontrado"
            )
        return produto

    def listar_produtos(self, db: Session) -> list[Produto]:
        return produto_repository.listar_todos(db)

    def atualizar_produto(self, db: Session, produto_id: int, dados: ProdutoUpdate) -> Produto:
        produto = produto_repository.atualizar(db, produto_id, dados)
        if not produto:
            raise HTTPException(
                status_code=404,
                detail=f"Produto {produto_id} não encontrado"
            )
        return produto

    def deletar_produto(self, db: Session, produto_id: int) -> dict:
        deletado = produto_repository.deletar(db, produto_id)
        if not deletado:
            raise HTTPException(
                status_code=404,
                detail=f"Produto {produto_id} não encontrado"
            )
        return {"mensagem": f"Produto {produto_id} deletado com sucesso"}

    def listar_produtos_criticos(self, db: Session) -> list[Produto]:
        produtos = produto_repository.listar_abaixo_estoque_minimo(db)
        return produtos

produto_service = ProdutoService()