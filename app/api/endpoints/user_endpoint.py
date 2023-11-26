from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from app.core.services.organization_service import OrganizationService
from app.core.services.user_service import UserService
from app.models.user import UserByOrganizationResponse, UserRequest, UserResponse

router = APIRouter(
    prefix="/api/users",
    tags=['Users']
)

user_service: UserService = Depends(UserService)
organization_service: OrganizationService = Depends(OrganizationService)

@router.get("/organization/{id}", status_code=status.HTTP_200_OK, response_model=UserByOrganizationResponse)
async def get_users_by_organization_id(
    id: int,
    user_service: UserService = user_service,
    organization_service: OrganizationService = organization_service
) -> UserByOrganizationResponse:
    organization = await organization_service.get_organization_by_id(id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organization with id {id} was not found")
    users = await user_service.get_users_by_organization_id(id)
    return {'organization': organization, 'users': users}

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(
    id: int,
    user_service: UserService = user_service
) -> UserResponse:
    user = await user_service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} was not found")
    return user

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    new_user: UserRequest,
    user_service: UserService = user_service,
    organization_service: OrganizationService = organization_service
) -> UserResponse:
    organization = await organization_service.get_organization_by_id(new_user.organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organization with id {new_user.organization_id} was not found")
    db_user = await user_service.get_user_by_email(new_user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email {new_user.email} already exists")
    user = await user_service.create_user(new_user)
    return user

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def update_user_by_id(
    id: int, 
    updated_user: UserRequest,
    user_service: UserService = user_service
) -> UserResponse:
    user = await user_service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} was not found")
    user = await user_service.update_user_by_id(id, updated_user)
    return user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_user_by_id(
    id: int,
    user_service: UserService = user_service
) -> None:
    user = await user_service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} was not found")
    await user_service.delete_user_by_id(id)

@router.delete("", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_users(
    user_service: UserService = user_service
) -> None:
    await user_service.delete_users()
