from fastapi import APIRouter
from models import Pedidos
from extensions import SessionDep
from sqlmodel import select
from decimal import Decimal

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Pedidos]:
    pedidos = session.exec(select(Pedidos)).all()
    return pedidos

@router.post('/')
async def cadastrar(session:SessionDep, usuario:int, total:Decimal) -> Pedidos:
    pedido = Pedidos(usuario_id=usuario, total=total, status='em andamento')
    session.add(pedido)
    session.commit()
    session.refresh(pedido)
    return pedido  

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     pedido = session.get(Pedidos, id)
     session.delete(pedido)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, total:Decimal, status:str) -> Pedidos:
    pedUpdate = session.get(Pedidos, id)
    pedUpdate.total = total
    pedUpdate.status = status
    session.add(pedUpdate)
    session.commit()
    session.refresh(pedUpdate)
    return pedUpdate

