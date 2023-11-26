from typing import List
from fastapi import Depends
from app.core.repositories.role_repository import RoleRepository
from app.core.services.interfaces.role_service_interface import RoleServiceInterface
from app.models.role import RoleRequest, RoleResponse


class RoleService(RoleServiceInterface):

    def __init__(
        self,
        role_repository: RoleRepository = Depends(RoleRepository)
    ):
        self.role_repository = role_repository
    
    async def get_role_by_id(
        self,
        id: int
    ) -> RoleResponse:
        role = await self.role_repository.get_role_by_id(id)
        return role

    async def get_roles_by_organization_id(
        self,
        organization_id: int
    ) -> List[RoleResponse]:
        roles = await self.role_repository.get_roles_by_organization_id(organization_id)
        return roles
    
    async def get_role_by_name_organization_id(
        self,
        name: str,
        organization_id: int
    ) -> RoleResponse:
        role = await self.role_repository.get_role_by_name_organization_id(name, organization_id)
        return role
    
    async def create_role(
        self,
        role: RoleRequest
    ) -> RoleResponse:
        return await self.role_repository.create_role(role)
    
    async def delete_role_by_id(
        self,
        id: int
    ) -> None:
        await self.role_repository.delete_role_by_id(id)

    async def delete_roles_by_organization_id(
        self,
        organization_id: int
    ) -> None:
        await self.role_repository.delete_roles_by_organization_id(organization_id)