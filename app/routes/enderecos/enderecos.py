from fastapi import APIRouter
from models import Endereco
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/enderecos",
    tags=["Endereco"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Endereco]:
    enderecos = session.exec(select(Endereco)).all()
    return enderecos

@router.post('/')
async def cadastrar(session:SessionDep, usuario_id:int, rua:str, cidade:str, estado:str, cep:str) -> Endereco:
    endereco = Endereco(usuario_id=usuario_id, rua=rua, cidade=cidade, estado=estado, cep=cep)
    session.add(endereco)
    session.commit()
    session.refresh(endereco)
    return endereco    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     endereco = session.get(Endereco, id)
     session.delete(endereco)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, usuario_id:int, rua:str, cidade:str, estado:str, cep:str) -> Endereco:
    enderecoUpdate = session.get(Endereco, id)
    enderecoUpdate.usuario_id = usuario_id
    enderecoUpdate.rua = rua
    enderecoUpdate.cidade = cidade
    enderecoUpdate.estado = estado
    enderecoUpdate.cep = cep
    session.add(enderecoUpdate)
    session.commit()
    session.refresh(enderecoUpdate)
    return enderecoUpdate


