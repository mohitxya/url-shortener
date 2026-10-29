from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
import redis

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
# manages physical connection pool and talks to the database.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# holds objects you read or modify during an operation. 

Base = declarative_base()
# maps python classes to table schemas. 

r = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()