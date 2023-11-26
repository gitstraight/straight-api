from typing import List
from fastapi import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.core.database.connector import get_db
from app.core.repositories.interfaces.user_repository_interface import UserRepositoryInterface
from app.models.user import UserRequest
from app.schemas.user import Users

class UserRepository(UserRepositoryInterface):

    def __init__(
        self, 
        db: Session = Depends(get_db)
    ):
        self.db = db

    async def get_users_by_organization_id(
        self,
        id: int
    ) -> List[Users]:
        return self.db.query(Users).filter(Users.organization_id == id).all()

    async def get_user_by_email(
        self,
        email: EmailStr
    ) -> Users:
        return self.db.query(Users).filter(Users.email == email).first()

    async def get_user_by_id(
        self, 
        id: int
    ) -> Users:
        return self.db.query(Users).filter(Users.id == id).first()

    async def create_user(
        self, 
        user: UserRequest
    ) -> Users:
        db_user = Users(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    async def update_user_by_id(
        self, 
        id: int, 
        updated_user: UserRequest
    ) -> Users:
        user = self.db.query(Users).filter(Users.id == id)
        if user.first():
            user.update(updated_user.model_dump(), synchronize_session=False)
            self.db.commit()
            return user.first()

    async def delete_user_by_id(
        self, 
        id: int
    ) -> None:
        user = self.db.query(Users).filter(Users.id == id).first()
        if user:
            self.db.delete(user)
            self.db.commit()

    async def delete_users(
        self
    ) -> None:
        self.db.query(Users).delete()
        self.db.commit()
