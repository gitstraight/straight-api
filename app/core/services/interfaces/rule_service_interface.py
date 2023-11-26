from abc import ABC, abstractmethod
from app.models.rule import RuleRequest, RuleResponseBase, RulesByOrganizationResponse

class RuleServiceInterface(ABC):

    @abstractmethod
    async def get_rules_by_organization_id(
        self, 
        organization_id
    ) -> RulesByOrganizationResponse:
        pass

    @abstractmethod
    async def get_rule_by_action_id_and_role_id(
        self, 
        action_id, 
        role_id
    ) -> RuleResponseBase:
        pass

    @abstractmethod
    async def create_rule(
        self, 
        rule: RuleRequest
    ) -> RuleResponseBase:
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
