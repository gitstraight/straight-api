from abc import ABC, abstractmethod
from typing import List
from app.models.user_role_organization import UserRoleOrganizationRequest, UserRoleOrganizationResponse

class RoleUserServiceInterface(ABC):

    @abstractmethod
    async def get_roles_by_user_id(
        self, 
        user_id: int
    ) -> List[UserRoleOrganizationResponse]:
        pass

    @abstractmethod
    async def get_user_role_organization_by_user_id_role_id(
        self, 
        user_id: int, 
        role_id: int
    ) -> UserRoleOrganizationResponse:
        pass

    @abstractmethod
    async def add_role_to_user(
        self, 
        role_user: UserRoleOrganizationRequest
    ) -> UserRoleOrganizationResponse:
        pass

    @abstractmethod
    async def delete_role_from_user(
        self, 
        role_user: UserRoleOrganizationRequest
    ) -> None:
        pass

    @abstractmethod
    async def delete_user_role_organization_by_user_id(
        self, 
        user_id: int
    ) -> None:
        pass
