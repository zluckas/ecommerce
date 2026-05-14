from fastapi import APIRouter
from models import Categorias
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Categorias]:
    categorias = session.exec(select(Categorias)).all()
    return categorias

@router.post('/')
async def cadastrar(session:SessionDep, nome:str) -> Categorias:
    categoria = Categorias(nome=nome)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria  

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     categoria = session.get(Categorias, id)
     session.delete(categoria)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str) -> Categorias:
    catUpdate = session.get(Categorias, id)
    catUpdate.nome = nome
    session.add(catUpdate)
    session.commit()
    session.refresh(catUpdate)
    return catUpdate

