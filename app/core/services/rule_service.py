from fastapi import Depends
from app.core.repositories.rule_repository import RuleRepository
from app.core.services.interfaces.rule_service_interface import RuleServiceInterface
from app.models.rule import RuleRequest

class RuleService(RuleServiceInterface):
    def __init__(self, rule_repository: RuleRepository = Depends(RuleRepository)):
        self.rule_repository = rule_repository

    async def get_rules_by_organization_id(
        self, 
        organization_id
    ):
        return await self.rule_repository.get_rules_by_organization_id(organization_id)
    
    async def get_rule_by_action_id_and_role_id(
        self,
        action_id,
        role_id
    ):
        return await self.rule_repository.get_rule_by_action_id_and_role_id(action_id, role_id)

    async def create_rule(
        self,
        rule: RuleRequest
    ):
        return await self.rule_repository.create_rule(rule)
    
    async def delete_rule_by_id(
        self,
        id
    ):
        return await self.rule_repository.delete_rule_by_id(id)
    
    async def delete_rules_by_organization_id(
        self,
        organization_id
    ):
        return await self.rule_repository.delete_rules_by_organization_id(organization_id)