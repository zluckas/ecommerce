from fastapi import FastAPI
from app.routes.categorias import categorias
from app.routes.papeis import papeis
from app.routes.pedidos import pedidos
from app.routes.produtos import produtos
from app.routes.usuarios import (
    usuarios
)
from app.dependencies.deps import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(usuarios.router)
app.include_router(papeis.router)
app.include_router(produtos.router)
app.include_router(categorias.router)
app.include_router(pedidos.router)



    