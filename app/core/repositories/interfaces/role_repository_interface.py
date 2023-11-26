from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.role import RoleRequest

from app.core.database.connector import get_db
from app.schemas.role import Roles


class RoleRepositoryInterface(ABC):

    @abstractmethod
    async def get_role_by_id(
        self,
        id: int
    ) -> Roles:
        pass
    
    @abstractmethod
    async def get_roles_by_organization_id(
        self,
        organization_id: int
    ) -> List[Roles]:
        pass

    @abstractmethod
    async def get_role_by_name_organization_id(
        self,
        name: str,
        organization_id: int
    ) -> Roles:
        pass
    
    @abstractmethod
    async def create_role(
        self,
        role: RoleRequest
    ) -> Roles:
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
            