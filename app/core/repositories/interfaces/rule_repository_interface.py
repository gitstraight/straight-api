
from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database.connector import get_db
from app.models.rule import RuleRequest
from app.schemas.action import Actions
from app.schemas.role import Roles
from app.schemas.rule import Rules


class RuleRepositoryInterface(ABC):

    @abstractmethod
    async def get_rules_by_organization_id(
        self, 
        organization_id
    ) -> List[Rules]:
        pass

    @abstractmethod
    async def get_rule_by_action_id_and_role_id(
        self, 
        action_id,
        role_id
    ) -> Rules:
        pass

    @abstractmethod
    async def create_rule(
        self, 
        rule: RuleRequest
    ) -> Rules:
        pass

    @abstractmethod
    async def delete_rule_by_id(
        self, 
        id
    ) -> None:
        pass

    @abstractmethod
    async def delete_rules_by_organization_id(
        self, 
        organization_id
    ) -> None:
        pass