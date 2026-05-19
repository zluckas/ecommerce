from sqlmodel import SQLModel, Session
from sqlmodel import create_engine, Session

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = '29062007'
DB_NAME = 'ecommerce'
DB_PORT = '3306'

sql_url = f"mysql+pymysql://root:usbw@localhost:3307/ecommerce"
engine = create_engine (sql_url)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session