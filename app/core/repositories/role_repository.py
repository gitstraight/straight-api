from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.repositories.interfaces.role_repository_interface import RoleRepositoryInterface
from app.models.role import RoleRequest
from app.schemas.role import Roles

from app.core.database.connector import get_db


class RoleRepository(RoleRepositoryInterface):

    def __init__(
        self,
        db: Session = Depends(get_db)
    ):
        self.db = db
    
    async def get_role_by_id(
        self,
        id: int
    ):
        role = self.db.query(Roles).filter(Roles.id == id).first()
        return role

    async def get_roles_by_organization_id(
        self,
        organization_id: int
    ):
        roles = self.db.query(Roles).filter(Roles.organization_id == organization_id).all()
        return roles

    async def get_role_by_name_organization_id(
        self,
        name: str,
        organization_id: int
    ):
        role = self.db.query(Roles).filter(Roles.name == name, Roles.organization_id == organization_id).first()
        return role
    
    async def create_role(
        self,
        role: RoleRequest
    ):
        new_role = Roles(**role.model_dump())
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role
    
    async def delete_role_by_id(
        self,
        id: int
    ):
        role = self.db.query(Roles).filter(Roles.id == id).first()
        self.db.delete(role)
        self.db.commit()

    async def delete_roles_by_organization_id(
        self,
        organization_id: int
    ):
        roles = self.db.query(Roles).filter(Roles.organization_id == organization_id).all()
        for role in roles:
            self.db.delete(role)
        self.db.commit()
            