from decimal import Decimal
from fastapi import APIRouter
from models import Pagamento
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamento"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Pagamento]:
    pagamentos = session.exec(select(Pagamento)).all()
    return pagamentos

@router.post('/')
async def cadastrar(session:SessionDep, pedido_id:int, valor:Decimal, metodo:str) -> Pagamento:
    pagamento = Pagamento(pedido_id=pedido_id, valor=valor, metodo=metodo, status="Pendente")
    session.add(pagamento)
    session.commit()
    session.refresh(pagamento)
    return pagamento    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     pagamento = session.get(Pagamento, id)
     session.delete(pagamento)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, pedido_id:int, valor:Decimal, metodo:str) -> Pagamento:
    pagamentoUpdate = session.get(Pagamento, id)
    pagamentoUpdate.pedido_id = pedido_id
    pagamentoUpdate.valor = valor
    pagamentoUpdate.metodo = metodo
    session.add(pagamentoUpdate)
    session.commit()
    session.refresh(pagamentoUpdate)
    return pagamentoUpdate


