from abc import ABC, abstractmethod
from typing import List

from app.models.organization import OrganizationRequest, OrganizationResponse
from app.schemas.organization import Organizations

class OrganizationRepositoryInterface(ABC):
    @abstractmethod
    async def get_organizations(
        self
    ) -> List[Organizations]:
        pass

    @abstractmethod
    async def get_organization_by_id(
        self, 
        id: int
    ) -> Organizations:
        pass

    @abstractmethod
    async def get_organization_by_name(
        self, 
        name: str
    ) -> Organizations:
        pass

    @abstractmethod
    async def create_organization(
        self, 
        organization: OrganizationRequest
    ) -> Organizations:
        pass

    @abstractmethod
    async def delete_organization_by_id(
        self, 
        id: int
    ) -> None:
        pass

    @abstractmethod
    async def delete_all_organizations(
        self
    ) -> None:
        pass
