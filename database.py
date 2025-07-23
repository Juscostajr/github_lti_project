from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

if __name__ == "__main__":
    from domain import models  # importa aqui para registrar
    print("📦 Tabelas no metadata:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
