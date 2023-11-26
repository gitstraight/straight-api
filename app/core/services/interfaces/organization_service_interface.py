from abc import ABC, abstractmethod
from typing import List

from app.models.organization import OrganizationRequest, OrganizationResponse

class OrganizationServiceInterface(ABC):
    
    @abstractmethod
    async def get_organizations(
        self
    ) -> List[OrganizationResponse]:
        pass

    @abstractmethod
    async def get_organization_by_id(
        self, 
        id: int
    ) -> OrganizationResponse:
        pass

    @abstractmethod
    async def get_organization_by_name(
        self, 
        name: str
    ) -> OrganizationResponse:
        pass

    @abstractmethod
    async def create_organization(
        self, 
        organization: OrganizationRequest
    ) -> OrganizationResponse:
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
