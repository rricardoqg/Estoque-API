from fastapi import FastAPI
from app.database import engine, Base
from app.routers import produto_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestão de Estoque",
    description="API para controle de estoque de pequenos negócios",
    version="1.0.0"
)

app.include_router(produto_router.router)

@app.get("/")
def root():
    return {"mensagem": "API de Estoque funcionando!"}