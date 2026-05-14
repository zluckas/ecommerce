from fastapi import APIRouter
from models import Usuarios
from pwdlib import PasswordHash
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

password_hash = PasswordHash.recommended()

@router.get('/')
def listar(session:SessionDep) -> list[Usuarios]:
    usuarios = session.exec(select(Usuarios)).all()
    return usuarios

@router.post('/')
async def cadastrar(session:SessionDep, usuario:Usuarios, nome:str, email:str, senha:str) -> Usuarios:
    hash = password_hash.hash(senha)
    usuario = Usuarios(nome=nome, email=email, senha_hash=hash)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
    usuario = session.get(Usuarios, id)
    session.delete(usuario)
    session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, nome:str, email:str) -> Usuarios:
    usuarioUpdate = session.get(Usuarios, id)
    usuarioUpdate.nome = nome
    usuarioUpdate.email = email
    session.add(usuarioUpdate)
    session.commit()
    session.refresh(usuarioUpdate)
    return usuarioUpdate