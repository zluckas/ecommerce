from fastapi import APIRouter
from models import Avaliacoes
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/avaliacoes",
    tags=["Avaliacoes"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Avaliacoes]:
    avaliacoes = session.exec(select(Avaliacoes)).all()
    return avaliacoes

@router.post('/')
async def cadastrar(session:SessionDep, usuario_id:int, produto_id:int, nota:int, comentario:str | None = None) -> Avaliacoes:
    avaliacao = Avaliacoes(usuario_id=usuario_id, produto_id=produto_id, nota=nota, comentario=comentario)
    session.add(avaliacao)
    session.commit()
    session.refresh(avaliacao)
    return avaliacao

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     avaliacao = session.get(Avaliacoes, id)
     session.delete(avaliacao)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, usuario_id:int, produto_id:int, nota:int, comentario:str | None = None) -> Avaliacoes:
    avaliacaoUpdate = session.get(Avaliacoes, id)
    avaliacaoUpdate.usuario_id = usuario_id
    avaliacaoUpdate.produto_id = produto_id
    avaliacaoUpdate.nota = nota
    avaliacaoUpdate.comentario = comentario
    session.add(avaliacaoUpdate)
    session.commit()
    session.refresh(avaliacaoUpdate)
    return avaliacaoUpdate 