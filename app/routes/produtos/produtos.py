from fastapi import APIRouter
from models import Produto
from deps.deps import SessionDep
from sqlmodel import select
from decimal import Decimal

router = APIRouter(
    prefix="/produtos",
    tags=["Produto"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Produto]:
    produtos = session.exec(select(Produto)).all()
    return produtos

@router.post('/')
async def cadastrar(session:SessionDep, nome:str, preco:Decimal, desc: str = None) -> Produto:
    produto = Produto(nome=nome, descricao=desc, preco=preco)
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto  

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     produto = session.get(Produto, id)
     session.delete(produto)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str, desc: str) -> Produto:
    prodUpdate = session.get(Produto, id)
    prodUpdate.nome = nome
    prodUpdate.descricao = desc
    session.add(prodUpdate)
    session.commit()
    session.refresh(prodUpdate)
    return prodUpdate

