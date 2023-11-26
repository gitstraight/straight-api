from fastapi import Depends
from pydantic import EmailStr
from app.core.services.interfaces.user_service_interface import UserServiceInterface
from app.utils import utils
from app.core.repositories.user_repository import UserRepository
from app.models.user import UserByOrganizationResponse, UserRequest, UserResponse

class UserService(UserServiceInterface):

    def __init__(
        self,
        user_repository: UserRepository = Depends(UserRepository),
    ):
        self.user_repository = user_repository
        self.utils = utils

    async def get_users_by_organization_id(
        self,
        id: int
    ) -> UserByOrganizationResponse:
        return await self.user_repository.get_users_by_organization_id(id)

    async def get_user_by_id(
        self, 
        id: int
    ) -> UserResponse:
        return await self.user_repository.get_user_by_id(id)
    
    async def get_user_by_email(
        self,
        email: EmailStr
    ) -> UserResponse:
        return await self.user_repository.get_user_by_email(email)

    async def create_user(
        self, 
        user: UserRequest
    ) -> UserResponse:
        user.password = utils.hashed_password(user.password)
        return await self.user_repository.create_user(user)
    
    async def update_user_by_id(
        self,
        id: int,
        updated_user: UserRequest
    ) -> UserResponse:
        updated_user.password = utils.hashed_password(updated_user.password)
        return await self.user_repository.update_user_by_id(id, updated_user)
    
    async def delete_user_by_id(
        self,
        id: int
    ) -> None:
        return await self.user_repository.delete_user_by_id(id)
    
    async def delete_users(
        self
    ) -> None:
        return await self.user_repository.delete_users()

