from sqlalchemy.orm import Session
from app.services.produto_service import produto_service
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from typing import List

class ProdutoController:

    def criar(self, db: Session, produto: ProdutoCreate) -> ProdutoResponse:
        return produto_service.criar_produto(db, produto)

    def buscar(self, db: Session, produto_id: int) -> ProdutoResponse:
        return produto_service.buscar_produto(db, produto_id)

    def listar(self, db: Session) -> List[ProdutoResponse]:
        return produto_service.listar_produtos(db)

    def atualizar(self, db: Session, produto_id: int, dados: ProdutoUpdate) -> ProdutoResponse:
        return produto_service.atualizar_produto(db, produto_id, dados)

    def deletar(self, db: Session, produto_id: int) -> dict:
        return produto_service.deletar_produto(db, produto_id)

    def listar_criticos(self, db: Session) -> List[ProdutoResponse]:
        return produto_service.listar_produtos_criticos(db)

produto_controller = ProdutoController()