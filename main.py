from fastapi import FastAPI
from src.routers.expenses import router as expenses_router

app = FastAPI()
app.include_router(expenses_router)

app.get("/")


async def root():
    return {"message": "Welcome to Expenses API"}
