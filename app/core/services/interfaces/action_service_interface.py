from abc import ABC, abstractmethod
from typing import List
from app.models.action import ActionRequest, ActionResponse, ActionsByOrganizationResponse, ActionsByUserResponse

class ActionServiceInterface(ABC):

    @abstractmethod
    async def get_action_by_id(
        self, 
        id: int
    ) -> ActionResponse:
        pass

    @abstractmethod
    async def get_actions_by_user_id(
        self, 
        user_id: int
    ) -> ActionsByUserResponse:
        pass

    @abstractmethod
    async def get_actions_by_organization_id(
        self, 
        
        organization_id: int
    ) -> ActionsByOrganizationResponse:
        pass

    @abstractmethod
    async def get_action_by_name_organization_id(
        self, 
        name: str, 
        organization_id: int
    ) -> ActionResponse:
        pass

    @abstractmethod
    async def create_action(
        self, 
        action: ActionRequest
    ) -> ActionResponse:
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
