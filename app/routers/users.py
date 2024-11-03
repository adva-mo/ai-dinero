from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.db.core import get_db
from app.db.users import (
    UserCreate,
    UserUpdate,
    create_db_user,
    read_db_user,
    update_db_user,
    delete_db_user
)

router = APIRouter(
    prefix="/users",
)


@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return read_db_user(user_id, db)


@router.post("")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_db_user(user, db)


@router.patch("/{user_id}")
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_db_user(user_id, user, db)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_db_user(user_id, db)
