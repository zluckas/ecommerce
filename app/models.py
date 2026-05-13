from sqlmodel import SQLModel, table, Field
from datetime import datetime, UTC
from decimal import Decimal

class Usuarios(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    nome:str
    email:str = Field(index=True, unique=True)
    senha_hash:str = Field(index=None)
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class Papeis(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    nome:str = Field(unique=True)

class UsuarioPapeis(SQLModel, table=True):
    usuario_id:int | None = Field(default=None, primary_key=True)
    papel_id:int = Field(foreign_key="papeis.id")

class Produtos(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    nome:str
    descricao:str | None = None    
    preco:Decimal = Field(default=0, max_digits=10, decimal_places=2) 
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class Categorias(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    nome:str 

class ProdutoCategorias(SQLModel, table=True):
    produto_id:int = Field(primary_key=True, foreign_key="produtos.id")
    categoria_id:int = Field(primary_key=True, foreign_key="categorias.id")

class Pedidos(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    usuario_id:int = Field(foreign_key="usuarios.id")
    total:Decimal = Field(default=0, max_digits=10, decimal_places=2)
    status:str
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class ItensPedido(SQLModel, table=True):
    id:str | None =  Field(default=None, primary_key=True)
    pedido_id:int = Field(foreign_key="pedidos.id")
    produto_id:int = Field(foreign_key="produtos.id")
    quantidade:int
    preco:Decimal = Field(default=0, max_digits=10, decimal_places=2)

class Pagamentos(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    pedido_id:int = Field(foreign_key="pedidos.id")
    valor:Decimal = Field(default=0, max_digits=10, decimal_places=2)
    metodo:str
    status:str
    pago_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class Enderecos(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    usuario_id:int = Field(foreign_key="usuarios.id")
    rua:str
    cidade:str
    estado:str
    cep:str

class Avaliacoes(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    usuario_id:int = Field(foreign_key="usuarios.id")
    produto_id:int = Field(foreign_key="produtos.id")
    nota:int
    comentario:str | None = None
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class Estoque(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    produto_id:int = Field(foreign_key="produtos.id", unique=True)
    quantidade:int
    atualizado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))
 