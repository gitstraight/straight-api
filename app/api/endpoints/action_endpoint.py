from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app.core.services.organization_service import OrganizationService
from app.core.services.action_service import ActionService
from app.core.services.user_service import UserService
from app.models.action import ActionRequest, ActionResponse, ActionsByOrganizationResponse, ActionsByUserResponse

router = APIRouter(
    prefix="/api/actions",
    tags=['Actions']
)

action_service: ActionService = Depends(ActionService)
organization_service: OrganizationService = Depends(OrganizationService)
user_service: UserService = Depends(UserService)

@router.get("/organizations/{organization_id}", status_code=status.HTTP_200_OK, response_model=ActionsByOrganizationResponse)
async def get_actions_by_organization_id(
    organization_id: int,
    action_service: ActionService = action_service,
    organization_service: OrganizationService = organization_service
) -> ActionsByOrganizationResponse:
    organization = await organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    actions = await action_service.get_actions_by_organization_id(organization_id)
    return {'organization': organization, 'actions': actions}

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=ActionsByUserResponse)
async def get_actions_by_user_id(
    user_id: int,
    action_service: ActionService = action_service,
    user_service: UserService = user_service
) -> ActionsByUserResponse:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    actions = await action_service.get_actions_by_user_id(user_id)
    return {'user': user, 'actions': actions}

@router.post("", status_code=status.HTTP_201_CREATED, response_model=ActionResponse)
async def create_action(
    new_action: ActionRequest,
    action_service: ActionService = action_service,
    organization_service: OrganizationService = organization_service
) -> ActionResponse:
    organization = await organization_service.get_organization_by_id(new_action.organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    db_action = await action_service.get_action_by_name_organization_id(new_action.name, new_action.organization_id)
    if db_action:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Action already exists")
    action = await action_service.create_action(new_action)
    return action

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_action_by_id(
    id: int,
    action_service: ActionService = action_service,
) -> None:
    action = await action_service.get_action_by_id(id)
    if not action:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")
    await action_service.delete_action_by_id(id)

@router.delete("/organization/{organization_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_actions_by_organization_id(
    organization_id: int,
    action_service: ActionService = action_service,
    organization_service: OrganizationService = organization_service
) -> None:
    organization = await organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    await action_service.delete_actions_by_organization_id(organization_id)