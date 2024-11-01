from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from .core import DBExpense   

class Expense(BaseModel):
    id: int
    actualPaymentAmount: float
    merchantName: str
    originalAmount: float

class ExpenseCreate(BaseModel):
    actualPaymentAmount: float
    merchantName: str
    originalAmount: float

    class Config:
        from_attributes = True

class ExpenseUpdate(BaseModel):
    actualPaymentAmount: float
    merchantName: str
    originalAmount: float

class ExpenseDelete(BaseModel):
    id: int 

def read_db_expense(expense_id: int,session: Session)-> Expense:
    db_expense= session.query(DBExpense).filter(DBExpense.id==expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_expense

def create_db_expense(expense: ExpenseCreate,session: Session)-> Expense:
    try:
        db_item= DBExpense(**expense.model_dump(exclude_none=True))
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def update_db_expense(id: int, expense: ExpenseUpdate, session: Session) -> Expense:
    db_expense = read_db_expense(id, session)
    for field, value in expense.model_dump(exclude_none=True).items():
        setattr(db_expense, field, value)
    session.commit()
    session.refresh(db_expense)
    return db_expense   

def delete_db_expense(id: int, session: Session) -> Expense:
    db_expense = read_db_expense(id, session)
    session.delete(db_expense)
    session.commit()
    return db_expense   