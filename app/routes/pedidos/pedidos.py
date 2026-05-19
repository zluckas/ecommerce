from fastapi import APIRouter
from models import Pedido
from deps.deps import SessionDep
from sqlmodel import select
from decimal import Decimal

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedido"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Pedido]:
    pedidos = session.exec(select(Pedido)).all()
    return pedidos

@router.post('/')
async def cadastrar(session:SessionDep, usuario:int, total:Decimal) -> Pedido:
    pedido = Pedido(usuario_id=usuario, total=total, status='em andamento')
    session.add(pedido)
    session.commit()
    session.refresh(pedido)
    return pedido  

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     pedido = session.get(Pedido, id)
     session.delete(pedido)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, total:Decimal, status:str) -> Pedido:
    pedUpdate = session.get(Pedido, id)
    pedUpdate.total = total
    pedUpdate.status = status
    session.add(pedUpdate)
    session.commit()
    session.refresh(pedUpdate)
    return pedUpdate

