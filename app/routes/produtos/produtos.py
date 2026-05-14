from fastapi import APIRouter
from models import Produtos
from app.dependencies.deps import SessionDep
from sqlmodel import select
from decimal import Decimal

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Produtos]:
    produtos = session.exec(select(Produtos)).all()
    return produtos

@router.post('/')
async def cadastrar(session:SessionDep, nome:str, desc: str, preco:Decimal) -> Produtos:
    produto = Produtos(nome=nome, descricao=desc, preco=preco)
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto  

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     produto = session.get(Produtos, id)
     session.delete(produto)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str, desc: str) -> Produtos:
    prodUpdate = session.get(Produtos, id)
    prodUpdate.nome = nome
    prodUpdate.descricao = desc
    session.add(prodUpdate)
    session.commit()
    session.refresh(prodUpdate)
    return prodUpdate

