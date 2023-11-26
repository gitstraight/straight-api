from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from app.core.database.config import database_settings
import os

SQL_ALCHEMY_DATABASE_URL = f'postgresql://{os.environ["DATABASE_USERNAME"]}:{os.environ["DATABASE_PASSWORD"]}@postgres:{os.environ["DATABASE_PORT"]}/{os.environ["DATABASE_NAME"]}'

# SQL_ALCHEMY_DATABASE_URL = f'postgresql://{database_settings.database_username}:{database_settings.database_password}@{database_settings.database_hostname}:{database_settings.database_port}/{database_settings.database_name}'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
