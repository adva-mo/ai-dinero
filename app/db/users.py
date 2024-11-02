from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from .core import DBUser


class UserBase(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int


class UserCreate(UserBase):
    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    pass


class UserDelete(BaseModel):
    id: int


def read_db_user(user_id: int, session: Session) -> User:
    db_user = session.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def create_db_user(user: UserCreate, session: Session) -> User:
    try:
        db_user = DBUser(**user.model_dump(exclude_none=True))
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


def update_db_user(user_id: int, user: UserUpdate, session: Session) -> User:
    db_user = read_db_user(user_id, session)
    for field, value in user.model_dump(exclude_none=True).items():
        setattr(db_user, field, value)
    session.commit()
    session.refresh(db_user)
    return db_user


def delete_db_user(user_id: int, session: Session) -> User:
    db_user = read_db_user(user_id, session)
    session.delete(db_user)
    session.commit()
    return db_user
