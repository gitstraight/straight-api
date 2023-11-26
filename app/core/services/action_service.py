from typing import List
from fastapi import Depends
from app.core.repositories.action_repository import ActionRepository
from app.core.services.interfaces.action_service_interface import ActionServiceInterface
from app.models.action import ActionRequest, ActionResponse, ActionsByOrganizationResponse, ActionsByUserResponse


class ActionService(ActionServiceInterface):

    def __init__(
        self,
        action_repository: ActionRepository = Depends(ActionRepository)
    ):
        self.action_repository = action_repository
    
    async def get_action_by_id(
        self,
        id: int
    ) -> ActionResponse:
        action = await self.action_repository.get_action_by_id(id)
        return action

    async def get_actions_by_user_id(
        self,
        user_id: int
    ) -> ActionsByUserResponse:
        actions = await self.action_repository.get_actions_by_user_id(user_id)
        return actions

    async def get_actions_by_organization_id(
        self,
        organization_id: int
    ) -> ActionsByOrganizationResponse:
        actions = await self.action_repository.get_actions_by_organization_id(organization_id)
        return actions
    
    async def get_action_by_name_organization_id(
        self,
        name: str,
        organization_id: int
    ) -> ActionResponse:
        action = await self.action_repository.get_action_by_name_organization_id(name, organization_id)
        return action
    
    async def create_action(
        self,
        action: ActionRequest
    ) -> ActionResponse:
        return await self.action_repository.create_action(action)
    
    async def delete_action_by_id(
        self,
        id: int
    ) -> None:
        await self.action_repository.delete_action_by_id(id)

    async def delete_actions_by_organization_id(
        self,
        organization_id: int
    ) -> None:
        await self.action_repository.delete_actions_by_organization_id(organization_id)