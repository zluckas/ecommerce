from sqlmodel import SQLModel, table, Field, Relationship
from typing import Optional, List
from datetime import datetime, UTC
from decimal import Decimal

class UsuarioPapel(SQLModel, table=True):
    __tablename__ = 'usuario_papeis'
    usuario_id:int = Field(default=None, primary_key=True)
    papel_id:int = Field(foreign_key="papeis.id")

class Usuario(SQLModel, table=True):
    __tablename__ = 'usuarios'
    id:int | None = Field(default=None, primary_key=True)
    nome:str
    email:str = Field(index=True, unique=True)
    senha_hash:str = Field(index=None)
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

    papeis: List[Papel] = Relationship(back_populates='usuarios', link_model=UsuarioPapel)

class Papel(SQLModel, table=True):
    __tablename__ = 'papeis'
    id: Optional[int] | None = Field(default=None, primary_key=True)
    nome:str = Field(unique=True)

    usuarios: List[Usuario] = Relationship(back_populates='papeis', link_model=UsuarioPapel)

class ProdutoCategoria(SQLModel, table=True):
    __tablename__ = 'produto_categorias'
    produto_id:int = Field(primary_key=True, foreign_key="produtos.id")
    categoria_id:int = Field(primary_key=True, foreign_key="categorias.id")

class Produto(SQLModel, table=True):
    __tablename__ = 'produtos'
    id:int | None = Field(default=None, primary_key=True)
    nome:str
    descricao:str | None = None    
    preco:Decimal = Field(default=0, max_digits=10, decimal_places=2) 
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

    categorias: List[Categoria] = Relationship(back_populates='produtos', link_model=ProdutoCategoria)

class Categoria(SQLModel, table=True):
    __tablename__ = 'categorias'
    id:int | None = Field(default=None, primary_key=True)
    nome:str 

    produtos: List[Produto] = Relationship(back_populates='categorias', link_model=ProdutoCategoria)

class Pedido(SQLModel, table=True):
    __tablename__ = 'pedidos'
    id:int | None = Field(default=None, primary_key=True)
    usuario_id:int = Field(foreign_key="usuarios.id")
    total:Decimal = Field(default=0, max_digits=10, decimal_places=2)
    status:str
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class ItemPedido(SQLModel, table=True):
    __tablename__ = 'itens_pedido'
    id:str | None =  Field(default=None, primary_key=True)
    pedido_id:int = Field(foreign_key="pedidos.id")
    produto_id:int = Field(foreign_key="produtos.id")
    quantidade:int
    preco:Decimal = Field(default=0, max_digits=10, decimal_places=2)

class Pagamento(SQLModel, table=True):
    __tablename__ = 'pagamentos'
    id:int | None = Field(default=None, primary_key=True)
    pedido_id:int = Field(foreign_key="pedidos.id")
    valor:Decimal = Field(default=0, max_digits=10, decimal_places=2)
    metodo:str
    status:str
    pago_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class Endereco(SQLModel, table=True):
    __tablename__ = 'enderecos'
    id:int | None = Field(default=None, primary_key=True)
    usuario_id:int = Field(foreign_key="usuarios.id")
    rua:str
    cidade:str
    estado:str
    cep:str

class Avaliacao(SQLModel, table=True):
    __tablename__ = 'avaliacoes'
    id:int | None = Field(default=None, primary_key=True)
    usuario_id:int = Field(foreign_key="usuarios.id")
    produto_id:int = Field(foreign_key="produtos.id")
    nota:int
    comentario:str | None = None
    criado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))

class Estoque(SQLModel, table=True):
    __tablename__ = 'estoque'
    id:int | None = Field(default=None, primary_key=True)
    produto_id:int = Field(foreign_key="produtos.id", unique=True)
    quantidade:int
    atualizado_em:datetime = Field(default_factory=lambda: datetime.now(UTC))
 