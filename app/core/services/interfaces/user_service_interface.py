from abc import ABC, abstractmethod
from typing import List

from pydantic import EmailStr
from app.models.user import UserRequest, UserResponse

class UserServiceInterface(ABC):

    @abstractmethod
    async def get_users_by_organization_id(
        self, 
        id: int
    ) -> List[UserResponse]:
        pass

    @abstractmethod
    async def get_user_by_id(
        self, 
        id: int
    ) -> UserResponse:
        pass

    @abstractmethod
    async def get_user_by_email(
        self, 
        email: EmailStr
    ) -> UserResponse:
        pass

    @abstractmethod
    async def create_user(
        self, 
        user: UserRequest
    ) -> UserResponse:
        pass

    @abstractmethod
    async def update_user_by_id(
        self, 
        id: int, 
        updated_user: UserRequest
    ) -> UserResponse:
        pass

    @abstractmethod
    async def delete_user_by_id(
        self, 
        id: int
    ) -> None:
        pass

    @abstractmethod
    async def delete_users(
        self
    ) -> None:
        pass
