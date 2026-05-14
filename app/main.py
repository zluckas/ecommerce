from fastapi import FastAPI
from routes.usuarios import usuarios
from routes.papeis import papeis
from routes.produtos import produtos
from routes.categorias import categorias
from routes.pedidos import pedidos  
from deps.deps import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(usuarios.router)
app.include_router(papeis.router)
app.include_router(produtos.router)
app.include_router(categorias.router)
app.include_router(pedidos.router)



    