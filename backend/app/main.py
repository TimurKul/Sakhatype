from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas, auth
from config import settings

app = FastAPI(
    title='Sakhatype',
    version='1.0',
    servers=[{'url': 'localhost:8080/docs'}]
)

@app.post('/auth/login')
def login(user_data: schemas.UserCreate):
    if user_data.username == 'admin' and user_data.password == 'admin':
        return {'access_token': auth.create_access_token('admin'), 'token_type': 'Bearer'}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password'
        )

@app.get('/users/me')
def get_current_user_info(username: str = Depends(auth.get_current_username)):
    return {'username': username}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
