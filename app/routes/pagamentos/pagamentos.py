from decimal import Decimal
from fastapi import APIRouter
from models import Pagamentos
from deps.deps import SessionDep
from sqlmodel import select

router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamentos"]
)

@router.get('/')
def listar(session:SessionDep) -> list[Pagamentos]:
    pagamentos = session.exec(select(Pagamentos)).all()
    return pagamentos

@router.post('/')
async def cadastrar(session:SessionDep, pedido_id:int, valor:Decimal, metodo:str) -> Pagamentos:
    pagamento = Pagamentos(pedido_id=pedido_id, valor=valor, metodo=metodo, status="Pendente")
    session.add(pagamento)
    session.commit()
    session.refresh(pagamento)
    return pagamento    

@router.delete('/{id}')
async def excluir(session:SessionDep, id:int):
     pagamento = session.get(Pagamentos, id)
     session.delete(pagamento)
     session.commit()

@router.put('/')
async def atualizar(session:SessionDep, id:int, pedido_id:int, valor:Decimal, metodo:str) -> Pagamentos:
    pagamentoUpdate = session.get(Pagamentos, id)
    pagamentoUpdate.pedido_id = pedido_id
    pagamentoUpdate.valor = valor
    pagamentoUpdate.metodo = metodo
    session.add(pagamentoUpdate)
    session.commit()
    session.refresh(pagamentoUpdate)
    return pagamentoUpdate


