from fastapi import APIRouter
from ExpensesManager import ExpensesManager

expenses_manager = ExpensesManager()
expenses_manager.load_expenses_from_json('expenses.json')


router = APIRouter(
    prefix="/expenses",
)

@router.get("/")
async def get_expenses():
    expenses = expenses_manager.get_all_expenses()
    return {"expenses": expenses}

@router.get("/{id}")
async def get_expense(id: int):
    expense = expenses_manager.get_expense_by_id(id)
    return {"expense": expense} 

@router.get("/total")
async def get_total():
    total = expenses_manager.get_total_amount()
    return {"total": total}
