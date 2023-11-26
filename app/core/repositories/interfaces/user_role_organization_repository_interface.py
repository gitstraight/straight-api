from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from app.core.database.connector import get_db
from sqlalchemy.orm import Session
from app.models.user_role_organization import UserRoleOrganizationRequest

from app.schemas.user_role_organization import UserRoleOrganization

class UserRoleOrganizationRepositoryInterface(ABC):

    @abstractmethod
    async def get_roles_by_user_id(
        self, 
        user_id: int
    ) -> List[UserRoleOrganization]:
        pass
    
    @abstractmethod
    async def get_user_role_organization_by_user_id_role_id(
        self, 
        user_id: int, 
        role_id: int
    ) -> UserRoleOrganization:
        pass

    @abstractmethod
    async def add_role_to_user(
        self, 
        user_role_organization: UserRoleOrganizationRequest
    ) -> UserRoleOrganization:
        pass

    @abstractmethod
    async def delete_role_from_user(
        self, 
        user_role_organization: UserRoleOrganizationRequest
    ) -> None:
        pass

    @abstractmethod
    async def delete_user_role_organization_by_user_id(
        self, 
        user_id: int
    ) -> None:
        pass
