from pydantic_settings import BaseSettings
import secrets

class Settings(BaseSettings):
    database_url: str = 'sqlite:///./sakhatype.db'
    secret_key: str = secrets.token_urlsafe(32)
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30

settings = Settings()
