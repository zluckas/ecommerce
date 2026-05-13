from fastapi import FastAPI
from routes import (
    papeis, usuarios, produtos, categorias, pedidos
)
from extensions import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(usuarios.router)
app.include_router(papeis.router)
app.include_router(produtos.router)
app.include_router(categorias.router)
app.include_router(pedidos.router)



    