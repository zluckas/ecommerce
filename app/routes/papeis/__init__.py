from fastapi import APIRouter
from models import Papeis
from extensions import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/papeis",
    tags=["Papeis"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Papeis]:
    papeis = session.exec(select(Papeis)).all()
    return papeis

@router.post('/')
async def cadastrar(session:SessionDep, nome:str) -> Papeis:
    papel = Papeis(nome=nome)
    session.add(papel)
    session.commit()
    session.refresh(papel)
    return papel    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     papel = session.get(Papeis, id)
     session.delete(papel)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str) -> Papeis:
    papelUpdate = session.get(Papeis, id)
    papelUpdate.nome = nome
    session.add(papelUpdate)
    session.commit()
    session.refresh(papelUpdate)
    return papelUpdate


