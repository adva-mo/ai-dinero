from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from .core import DBCategory


class CategoryBase(BaseModel):
    name: str
    external_id: int


class Category(CategoryBase):
    id: int


class CategoryCreate(CategoryBase):
    class Config:
        from_attributes = True


class CategoryUpdate(CategoryBase):
    pass


class CategoryDelete(BaseModel):
    id: int


def read_db_category(category_id: int, session: Session) -> Category:
    db_category = session.query(DBCategory).filter(
        DBCategory.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


def create_db_category(category: CategoryCreate, session: Session) -> Category:
    try:
        db_category = DBCategory(**category.model_dump(exclude_none=True))
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


def update_db_category(id: int, category: CategoryUpdate, session: Session) -> Category:
    db_category = read_db_category(id, session)
    for field, value in category.model_dump(exclude_none=True).items():
        setattr(db_category, field, value)
    session.commit()
    session.refresh(db_category)
    return db_category


def delete_db_category(id: int, session: Session) -> Category:
    db_category = read_db_category(id, session)
    session.delete(db_category)
    session.commit()
    return db_category
