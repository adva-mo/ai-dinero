from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.core import get_db, DBExpense
from db.expenses import Expense, ExpenseCreate, create_db_expense, read_db_expense

router = APIRouter(
    prefix="/expenses",
)

@router.get("/")
async def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(DBExpense).all()
    return {"expenses": expenses}

@router.post("/")
async def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_db_expense(expense, db)

@router.get("/{expense_id}")
async def get_expense(expense_id: int, db: Session = Depends(get_db)):
    return read_db_expense(expense_id, db)
