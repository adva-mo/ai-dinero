from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.core import get_db, DBCategory
from app.db.categories import (
    Category,
    CategoryCreate,
    CategoryUpdate,
    create_db_category,
    read_db_category,
    update_db_category,
    delete_db_category
)
from app.utils.decorators import handle_single_or_list

router = APIRouter(
    prefix="/categories",
)


@router.get("/{category_id}")
async def get_category(category_id: int, db: Session = Depends(get_db)):
    return read_db_category(category_id, db)


@router.post("")
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_db_category(category, db)


@router.patch("/{category_id}")
async def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return update_db_category(category_id, category, db)


@router.delete("/{category_id}")
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    return delete_db_category(category_id, db)
