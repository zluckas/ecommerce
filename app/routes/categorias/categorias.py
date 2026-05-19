from fastapi import APIRouter
from models import Categoria
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/categorias",
    tags=["Categoria"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Categoria]:
    categorias = session.exec(select(Categoria)).all()
    return categorias

@router.post('/')
async def cadastrar(session:SessionDep, nome:str) -> Categoria:
    categoria = Categoria(nome=nome)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria  

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     categoria = session.get(Categoria, id)
     session.delete(categoria)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str) -> Categoria:
    catUpdate = session.get(Categoria, id)
    catUpdate.nome = nome
    session.add(catUpdate)
    session.commit()
    session.refresh(catUpdate)
    return catUpdate

