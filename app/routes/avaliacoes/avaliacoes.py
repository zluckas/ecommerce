from fastapi import APIRouter
from models import Avaliacao
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/avaliacoes",
    tags=["Avaliacao"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Avaliacao]:
    avaliacoes = session.exec(select(Avaliacao)).all()
    return avaliacoes

@router.post('/')
async def cadastrar(session:SessionDep, usuario_id:int, produto_id:int, nota:int, comentario:str | None = None) -> Avaliacao:
    avaliacao = Avaliacao(usuario_id=usuario_id, produto_id=produto_id, nota=nota, comentario=comentario)
    session.add(avaliacao)
    session.commit()
    session.refresh(avaliacao)
    return avaliacao

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     avaliacao = session.get(Avaliacao, id)
     session.delete(avaliacao)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, usuario_id:int, produto_id:int, nota:int, comentario:str | None = None) -> Avaliacao:
    avaliacaoUpdate = session.get(Avaliacao, id)
    avaliacaoUpdate.usuario_id = usuario_id
    avaliacaoUpdate.produto_id = produto_id
    avaliacaoUpdate.nota = nota
    avaliacaoUpdate.comentario = comentario
    session.add(avaliacaoUpdate)
    session.commit()
    session.refresh(avaliacaoUpdate)
    return avaliacaoUpdate 