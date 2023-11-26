from fastapi import Depends
from app.core.repositories.user_role_organization_repository import UserRoleOrganizationRepository
from app.core.services.interfaces.user_role_organization_service_interface import RoleUserServiceInterface
from app.models.user_role_organization import UserRoleOrganizationRequest, UserRoleOrganizationResponse

class UserRoleOrganizationService(RoleUserServiceInterface):

    def __init__(
        self, 
        role_user_repository: UserRoleOrganizationRepository = Depends(UserRoleOrganizationRepository)
    ):
        self.role_user_repository = role_user_repository

    async def get_roles_by_user_id(
        self, 
        user_id: int
    ):
        return await self.role_user_repository.get_roles_by_user_id(user_id)
    
    async def get_user_role_organization_by_user_id_role_id(
        self, 
        user_id: int, 
        role_id: int
    ):
        return await self.role_user_repository.get_user_role_organization_by_user_id_role_id(user_id, role_id)

    async def add_role_to_user(
        self, 
        role_user: UserRoleOrganizationRequest
    ) -> UserRoleOrganizationResponse:
        return await self.role_user_repository.add_role_to_user(role_user)
    
    async def delete_role_from_user(
        self, 
        role_user: UserRoleOrganizationRequest
    ):
        return await self.role_user_repository.delete_role_from_user(role_user)
    
    async def delete_user_role_organization_by_user_id(
        self, 
        user_id: int
    ):
        return await self.role_user_repository.delete_user_role_organization_by_user_id(user_id)