from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    database_hostname: str = 'localhost'
    database_port: str = '5432'
    database_username: str = 'postgres'
    database_password: str = 'Wysescale'
    database_name: str = 'fastapi'
    secret_key: str = 'c5ac49e468d664c7186a475dff7f33d29ede3f2a88aea4afb4b05d2e150f7095'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30
    class Config:
        env_file = "C:\\PYDEV\\MongoDB\\SAJAPI\\.env"
        # env_file = ".env"

load_dotenv()

settings = Settings()



