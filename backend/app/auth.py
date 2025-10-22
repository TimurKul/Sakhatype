from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, timedelta

import schemas
from config import settings

security = HTTPBearer()
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Count not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'}
)

def create_access_token(username: str):
    return jwt.encode(
        {'sub': username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
        settings.secret_key,
        algorithm=settings.algorithm
    )

def get_current_username(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, settings.secret_key, algorithms=[settings.algorithm])
        username: Optional[str] = payload.get('sub')
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception
