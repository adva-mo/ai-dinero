import os
from fastapi import FastAPI
from app.routers.expenses import router as expenses_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers.users import router as users_router
from app.routers.categories import router as categories_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_SERVER")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expenses_router)
app.include_router(users_router)
app.include_router(categories_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Expenses API"}
