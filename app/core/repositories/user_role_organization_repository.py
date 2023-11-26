from fastapi import Depends
from app.core.database.connector import get_db
from sqlalchemy.orm import Session
from app.core.repositories.interfaces.user_role_organization_repository_interface import UserRoleOrganizationRepositoryInterface
from app.models.user_role_organization import UserRoleOrganizationRequest

from app.schemas.user_role_organization import UserRoleOrganization


class UserRoleOrganizationRepository(UserRoleOrganizationRepositoryInterface):
    def __init__(
        self, 
        db: Session = Depends(get_db)
    ):
        self.db = db

    async def get_roles_by_user_id(
        self, 
        user_id: int
    ):
        return self.db.query(UserRoleOrganization).filter(UserRoleOrganization.user_id == user_id).all()
    
    async def get_user_role_organization_by_user_id_role_id(
        self, 
        user_id: int, 
        role_id: int
    ):
        return self.db.query(UserRoleOrganization).filter(UserRoleOrganization.user_id == user_id, UserRoleOrganization.role_id == role_id).first()

    async def add_role_to_user(
        self, 
        user_role_organization: UserRoleOrganizationRequest
    ):
        new_user_role_organization = UserRoleOrganization(**user_role_organization.model_dump())
        self.db.add(new_user_role_organization)
        self.db.commit()
        self.db.refresh(new_user_role_organization)
        return new_user_role_organization
    
    async def delete_role_from_user(
        self, 
        user_role_organization: UserRoleOrganizationRequest
    ) -> None:
        self.db.query(UserRoleOrganization).filter(UserRoleOrganization.role_id== user_role_organization.role_id, UserRoleOrganization.user_id == user_role_organization.user_id).delete()
        self.db.commit()

    async def delete_user_role_organization_by_user_id(
        self, 
        user_id: int
    ) -> None:
        self.db.query(UserRoleOrganization).filter(UserRoleOrganization.user_id == user_id).delete()
        self.db.commit()