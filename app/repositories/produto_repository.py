from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate
from typing import Optional

class ProdutoRepository:

    def criar(self, db: Session, produto: ProdutoCreate) -> Produto:
        db_produto = Produto(**produto.model_dump())
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto

    def buscar_por_id(self, db: Session, produto_id: int) -> Optional[Produto]:
        return db.query(Produto).filter(Produto.id == produto_id).first()

    def listar_todos(self, db: Session) -> list[Produto]:
        return db.query(Produto).all()

    def atualizar(self, db: Session, produto_id: int, dados: ProdutoUpdate) -> Optional[Produto]:
        db_produto = self.buscar_por_id(db, produto_id)
        if not db_produto:
            return None
        dados_atualizados = dados.model_dump(exclude_unset=True)
        for campo, valor in dados_atualizados.items():
            setattr(db_produto, campo, valor)
        db.commit()
        db.refresh(db_produto)
        return db_produto

    def deletar(self, db: Session, produto_id: int) -> bool:
        db_produto = self.buscar_por_id(db, produto_id)
        if not db_produto:
            return False
        db.delete(db_produto)
        db.commit()
        return True

    def listar_abaixo_estoque_minimo(self, db: Session) -> list[Produto]:
        return db.query(Produto).filter(
            Produto.quantidade_estoque <= Produto.estoque_minimo
        ).all()

produto_repository = ProdutoRepository()