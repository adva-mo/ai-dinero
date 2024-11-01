from fastapi import APIRouter
from TransactionManager import TransactionManager

transaction_manager = TransactionManager()
transaction_manager.load_transactions_from_json('transactions.json')


router = APIRouter(
    prefix="/expenses",
)

@router.get("/")
async def get_expenses():
    transactions = transaction_manager.get_all_transactions()
    return {"transactions": transactions}

@router.get("/total")
async def get_total():
    total = transaction_manager.get_total_amount()
    return {"total": total}
