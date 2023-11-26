from abc import ABC, abstractmethod
from typing import List

from pydantic import EmailStr
from app.models.user import UserRequest

from app.schemas.user import Users

class UserRepositoryInterface(ABC):

    @abstractmethod
    async def get_users_by_organization_id(
        self, 
        id: int
    ) -> List[Users]:
        pass

    @abstractmethod
    async def get_user_by_email(
        self, 
        email: EmailStr
    ) -> Users:
        pass

    @abstractmethod
    async def get_user_by_id(
        self, 
        id: int
    ) -> Users:
        pass

    @abstractmethod
    async def create_user(
        self, 
        user: UserRequest
    ) -> Users:
        pass

    @abstractmethod
    async def update_user_by_id(
        self, 
        id: int, 
        updated_user: UserRequest
    ) -> Users:
        pass

    @abstractmethod
    def delete_user_by_id(
        self, 
        id: int
    ) -> None:
        pass

    @abstractmethod
    def delete_users(
        self
    ):
        pass
