from fastapi import APIRouter
from models import Usuario
from pwdlib import PasswordHash
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuario"]
)

senha_context = PasswordHash.recommended()

@router.get('/')
def listar(session:SessionDep) -> list[Usuario]:
    usuarios = session.exec(select(Usuario)).all()
    return usuarios

@router.post('/')
async def cadastrar(session:SessionDep, usuario:Usuario, nome:str, email:str, senha:str) -> Usuario:
    senha_hash = senha_context.hash(senha)
    usuario = Usuario(nome=nome, email=email, senha_hash=senha_hash)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
    usuario = session.get(Usuario, id)
    session.delete(usuario)
    session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str, email:str) -> Usuario:
    usuarioUpdate = session.get(Usuario, id)
    usuarioUpdate.nome = nome
    usuarioUpdate.email = email
    session.add(usuarioUpdate)
    session.commit()
    session.refresh(usuarioUpdate)
    return usuarioUpdate