from abc import ABC, abstractmethod
from typing import List
from app.models.role import RoleRequest, RoleResponse

class RoleServiceInterface(ABC):

    @abstractmethod
    async def get_role_by_id(
        self, 
        id: int
    ) -> RoleResponse:
        pass

    @abstractmethod
    async def get_roles_by_organization_id(
        self, 
        organization_id: int
    ) -> List[RoleResponse]:
        pass

    @abstractmethod
    async def get_role_by_name_organization_id(
        self, 
        name: str, 
        organization_id: int
    ) -> RoleResponse:
        pass

    @abstractmethod
    async def create_role(
        self, 
        role: RoleRequest
    ) -> RoleResponse:
        pass

    @abstractmethod
    async def delete_role_by_id(
        self, 
        id: int
    ) -> None:
        pass

    @abstractmethod
    async def delete_roles_by_organization_id(
        self, 
        organization_id: int
    ) -> None:
        pass
