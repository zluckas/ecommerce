from fastapi import APIRouter
from models import Enderecos
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/enderecos",
    tags=["Enderecos"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Enderecos]:
    enderecos = session.exec(select(Enderecos)).all()
    return enderecos

@router.post('/')
async def cadastrar(session:SessionDep, usuario_id:int, rua:str, cidade:str, estado:str, cep:str) -> Enderecos:
    endereco = Enderecos(usuario_id=usuario_id, rua=rua, cidade=cidade, estado=estado, cep=cep)
    session.add(endereco)
    session.commit()
    session.refresh(endereco)
    return endereco    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     endereco = session.get(Enderecos, id)
     session.delete(endereco)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, usuario_id:int, rua:str, cidade:str, estado:str, cep:str) -> Enderecos:
    enderecoUpdate = session.get(Enderecos, id)
    enderecoUpdate.usuario_id = usuario_id
    enderecoUpdate.rua = rua
    enderecoUpdate.cidade = cidade
    enderecoUpdate.estado = estado
    enderecoUpdate.cep = cep
    session.add(enderecoUpdate)
    session.commit()
    session.refresh(enderecoUpdate)
    return enderecoUpdate


