from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_username: str
    database_password: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    class Config:
        # env_file = "C:\\PYDEV\\MongoDB\\SAJAPI\\.env"
        env_file = ".env"

load_dotenv()

settings = Settings()

