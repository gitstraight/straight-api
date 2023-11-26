
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database.connector import get_db
from app.core.repositories.interfaces.rule_repository_interface import RuleRepositoryInterface
from app.models.rule import RuleRequest
from app.schemas.action import Actions
from app.schemas.role import Roles
from app.schemas.rule import Rules

class RuleRepository(RuleRepositoryInterface):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def get_rules_by_organization_id(
        self, 
        organization_id
    ):
        rules = (
            self.db
            .query(Rules)
            .join(Actions)
            .join(Roles)
            .filter(Actions.organization_id == organization_id, Roles.organization_id == organization_id)
            .all()
        )
        return rules

    async def get_rule_by_action_id_and_role_id(
        self, 
        action_id,
        role_id
    ):
        rule = (
            self.db
            .query(Rules)
            .filter(Rules.action_id == action_id, Rules.role_id == role_id)
            .first()
        )
        return rule

    async def create_rule(
        self, 
        rule: RuleRequest
    ):
        new_rule = Rules(**rule.model_dump())
        self.db.add(new_rule)
        self.db.commit()
        self.db.refresh(new_rule)
        return new_rule
    
    async def delete_rule_by_id(
        self, 
        id
    ):
        self.db.query(Rules).filter(Rules.id == id).delete()
        self.db.commit()

    async def delete_rules_by_organization_id(
        self,
        organization_id
    ):
        (
            self.db
            .query(Rules)
            .join(Actions)
            .join(Roles)
            .filter(Actions.organization_id == organization_id, Roles.organization_id == organization_id)
            .delete()
        )
        self.db.commit()