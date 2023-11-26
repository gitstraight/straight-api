from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database.connector import get_db
from app.core.repositories.interfaces.organization_repository_interface import OrganizationRepositoryInterface
from app.models.organization import OrganizationRequest
from app.utils import utils

from app.schemas.organization import Organizations

class OrganizationRepository(OrganizationRepositoryInterface):

    def __init__(
        self, 
        db: Session = Depends(get_db)
    ):
        self.db = db

    async def get_organizations(
        self
    ) -> List[Organizations]:
        organizations = self.db.query(Organizations).all()
        return organizations

    async def get_organization_by_id(
        self, 
        id: int
    ) -> Organizations:
        organization = self.db.query(Organizations).filter(Organizations.id == id).first()
        return organization
    
    async def get_organization_by_name(
        self, 
        name: str
    ) -> Organizations:
        organization = self.db.query(Organizations).filter(Organizations.name == name).first()
        return organization

    async def create_organization(
        self, 
        organization: OrganizationRequest
    ) -> Organizations:
        new_organization = Organizations(**organization.model_dump())
        new_organization.api_key = utils.generate_api_key()
        self.db.add(new_organization)
        self.db.commit()
        self.db.refresh(new_organization)
        return new_organization

    async def delete_organization_by_id(
        self, 
        id: int
    ) -> None:
        organization = await self.get_organization_by_id(id)
        self.db.delete(organization)
        self.db.commit()

    async def delete_all_organizations(
        self
    ) -> None:
        self.db.query(Organizations).delete()
        self.db.commit()
