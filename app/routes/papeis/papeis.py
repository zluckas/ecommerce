from fastapi import APIRouter
from models import Papel
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/papeis",
    tags=["Papel"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Papel]:
    papeis = session.exec(select(Papel)).all()
    return papeis

@router.post('/')
async def cadastrar(session:SessionDep, nome:str) -> Papel:
    papel = Papel(nome=nome)
    session.add(papel)
    session.commit()
    session.refresh(papel)
    return papel    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     papel = session.get(Papel, id)
     session.delete(papel)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str) -> Papel:
    papelUpdate = session.get(Papel, id)
    papelUpdate.nome = nome
    session.add(papelUpdate)
    session.commit()
    session.refresh(papelUpdate)
    return papelUpdate


