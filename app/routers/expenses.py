from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.decorators import handle_single_or_list
from app.db.core import get_db, DBExpense
from app.db.expenses import (
    ExpenseCreate,
    ExpenseUpdate,
    create_db_expense,
    read_db_expense,
    update_db_expense,
    delete_db_expense
)

router = APIRouter(
    prefix="/expenses",
)


@router.get("/")
async def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(DBExpense).all()
    return {"expenses": expenses}


@router.post("/")
@handle_single_or_list
async def create_expense(expense: ExpenseCreate | list[ExpenseCreate], db: Session = Depends(get_db)):
    return create_db_expense([expense], db)


@router.get("/{expense_id}/")
async def get_expense(expense_id: int, db: Session = Depends(get_db)):
    return read_db_expense(expense_id, db)


@router.patch("/{expense_id}/")
async def update_expense(expense_id: int, expense: ExpenseUpdate, db: Session = Depends(get_db)):
    return update_db_expense(expense_id, expense, db)


@router.delete("/{expense_id}/")
async def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return delete_db_expense(expense_id, db)
