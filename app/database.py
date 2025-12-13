from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .domain_database import DATABASE_URL  # PostgreSQL URL, masalan: postgresql://user:pass@localhost:5432/dbname

SQLALCHEMY_DATABASE_URL = DATABASE_URL

# PostgreSQLda connect_args kerak emas
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
