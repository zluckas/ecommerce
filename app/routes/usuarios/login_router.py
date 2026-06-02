from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, Depends, status

from models import Usuario
from usuarios import router as usuario_router
from pwdlib import PasswordHash 
from typing import Annotated
from deps.deps import SessionDep
from sqlmodel import select
from tokenize import Token
from datetime import timedelta, datetime
import jwt


router = usuario_router
token_schema = OAuth2PasswordRequestForm(tokenUrl="token")
senha_context = PasswordHash.recommended()
SECRET_KEY = '0fuwef0wu8ene0uiwnf'
ALGORITIMO = 'HS256'


def get_usuario_logado(session: SessionDep, token: Annotated[str, Depends(token_schema)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITIMO])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        
        usuario = session.scalar(select(Usuario).where(Usuario.email == email))
        
        if usuario is None:
            raise credentials_exception
        return usuario
        
    except Exception:
        raise credentials_exception


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITIMO)
    return token


@router.post(path='/', response_model=Token)
async def login(session = SessionDep, form: OAuth2PasswordRequestForm = Depends()):
    usuario = session.scalar(select(Usuario).where(Usuario.email == form.username))
    if not usuario:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")
    if not senha_context.verify(form.password, usuario.senha_hash):
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")
    
    access_token = create_access_token(data={
        "sub": usuario.email})
    return {'access_token': access_token, 'token_type': 'bearer'}


