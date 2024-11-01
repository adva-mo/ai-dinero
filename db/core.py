import os
from sqlalchemy import create_engine, Float, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError("DB_URL environment variable is not set. Please set it before running the application.")

class Base(DeclarativeBase):
    pass

class DBExpense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    actualPaymentAmount: Mapped[float] 
    merchantName: Mapped[str] 
    originalAmount: Mapped[float]

engine = create_engine(DB_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()  