from sqlmodel import SQLModel, Session
from sqlmodel import create_engine, Session

sql_url = "mysql+pymysql://root:usbw@localhost:3307/ecommerce"
engine = create_engine (sql_url)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session