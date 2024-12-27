from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings

# SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@<host>:<port>/<database>'
# user_name = 'postgres:'
# password = 'Stesscale1%40'
# host = '@localhost:5432/'
# database = 'fastapi'
# SQLALCHEMY_DATABASE_URI1 = 'postgresql://'+user_name + password + host + database
SQLALCHEMY_DATABASE_URI = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
print(SQLALCHEMY_DATABASE_URI)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()