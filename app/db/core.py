import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError(
        "DB_URL environment variable is not set. Please set it before running the application.")


class Base(DeclarativeBase):
    pass


class DBExpense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("categories.id"))
    actual_amount: Mapped[float]
    original_amount: Mapped[float]
    original_currency: Mapped[str]
    merchant_name: Mapped[str]
    plan_name: Mapped[str]
    payment_date_time: Mapped[str]
    comments: Mapped[str]


class DBUser(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    expenses: Mapped[List[DBExpense]] = relationship()


class DBCategory(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    external_id: Mapped[int]
    expenses: Mapped[List[DBExpense]] = relationship()


engine = create_engine(DB_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
