from fastapi import Depends
from typing import List
from app.core.database.connector import get_db
from app.core.repositories.organization_repository import OrganizationRepository
from app.core.services.interfaces.organization_service_interface import OrganizationServiceInterface

from app.models.organization import OrganizationRequest, OrganizationResponse

class OrganizationService(OrganizationServiceInterface):

    def __init__(
        self, 
        organization_repository: OrganizationRepository = Depends(OrganizationRepository)
    ):
        self.organization_repository = organization_repository

    async def get_organizations(
        self
    ) -> List[OrganizationResponse]:
        organizations = await self.organization_repository.get_organizations()
        return organizations

    async def get_organization_by_id(
        self, 
        id: int
    ) -> OrganizationResponse:
        organization = await self.organization_repository.get_organization_by_id(id)
        return organization
  
    async def get_organization_by_name(
        self, 
        name: str
    ) -> OrganizationResponse:
        organization = await self.organization_repository.get_organization_by_name(name)
        return organization

    async def create_organization(
        self, 
        organization: OrganizationRequest
    ) -> OrganizationResponse:
        return await self.organization_repository.create_organization(organization)

    async def delete_organization_by_id(
        self, 
        id: int
    ) -> None:
        await self.organization_repository.delete_organization_by_id(id)

    async def delete_all_organizations(
        self
    ) -> None:
        await self.organization_repository.delete_all_organizations()
