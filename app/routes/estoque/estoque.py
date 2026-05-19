from fastapi import APIRouter
from models import Estoque
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Estoque]:
    estoque = session.exec(select(Estoque)).all()
    return estoque

@router.post('/')
async def cadastrar(session:SessionDep, produto_id:int, quantidade:int) -> Estoque:
    estoque = Estoque(produto_id=produto_id, quantidade=quantidade)
    session.add(estoque)
    session.commit()
    session.refresh(estoque)
    return estoque    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     estoque = session.get(Estoque, id)
     session.delete(estoque)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, produto_id:int, quantidade:int) -> Estoque:
    estoqueUpdate = session.get(Estoque, id)
    estoqueUpdate.produto_id = produto_id 
    estoqueUpdate.quantidade = quantidade 
    session.add(estoqueUpdate)
    session.commit()
    session.refresh(estoqueUpdate)
    return estoqueUpdate


