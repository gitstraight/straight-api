from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.action import ActionRequest
from app.schemas.action import Actions

from app.core.database.connector import get_db
from app.schemas.role import Roles
from app.schemas.user_role_organization import UserRoleOrganization
from app.schemas.rule import Rules
from app.schemas.user import Users


class ActionRepositoryInterface(ABC):
    
    @abstractmethod
    async def get_action_by_id(
        self,
        id: int
    ) -> Actions:
        pass
    
    @abstractmethod
    async def get_actions_by_user_id(
        self,
        user_id: int
    ) -> List[Actions]:
        pass
    
    @abstractmethod
    async def get_actions_by_organization_id(
        self,
        organization_id: int
    ) -> List[Actions]:
        pass

    @abstractmethod
    async def get_action_by_name_organization_id(
        self,
        name: str,
        organization_id: int
    ) -> Actions:
        pass
    
    @abstractmethod
    async def create_action(
        self,
        action: ActionRequest
    ) -> Actions:
        pass
    
    @abstractmethod
    async def delete_action_by_id(
        self,
        id: int
    ) -> None:
        pass

    @abstractmethod
    async def delete_actions_by_organization_id(
        self,
        organization_id: int
    ) -> None:
        pass
            