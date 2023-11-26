
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.services.role_service import RoleService

from app.core.services.user_role_organization_service import UserRoleOrganizationService
from app.core.services.user_service import UserService
from app.models.user_role_organization import UserRoleOrganizationRequest, UserRoleOrganizationResponse


router = APIRouter(
    prefix="/api/user_role_organization",
    tags=['UserRoleOrganization'],
)

user_role_organization_service: UserRoleOrganizationService = Depends(UserRoleOrganizationService)
user_service: UserService = Depends(UserService)
role_service: RoleService = Depends(RoleService)

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=List[UserRoleOrganizationResponse])
async def get_roles_by_user_id(
    user_id: int,
    user_role_organization_service: UserRoleOrganizationService = user_role_organization_service,
    user_service: UserService = user_service
) -> List[UserRoleOrganizationResponse]:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    return await user_role_organization_service.get_roles_by_user_id(user_id)

@router.post("", status_code=status.HTTP_201_CREATED)
async def add_role_to_user(
    user_role_organization: UserRoleOrganizationRequest,
    user_role_organization_service: UserRoleOrganizationService = user_role_organization_service,
    user_service: UserService = user_service,
    role_service: RoleService = role_service
) -> UserRoleOrganizationResponse:
    user = await user_service.get_user_by_id(user_role_organization.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_role_organization.user_id} not found")
    role = await role_service.get_role_by_id(user_role_organization.role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Role with id {user_role_organization.role_id} not found")
    if role.organization.id != user.organization.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Role with id {user_role_organization.role_id} does not belong to the same organization as user with id {user_role_organization.user_id}")
    db_user_role_organization = await user_role_organization_service.get_user_role_organization_by_user_id_role_id(user_role_organization.user_id, user_role_organization.role_id)
    if db_user_role_organization:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Role with id {user_role_organization.role_id} already assigned to user with id {user_role_organization.user_id}")
    return await user_role_organization_service.add_role_to_user(user_role_organization)

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role_from_user(
    user_role_organization: UserRoleOrganizationRequest,
    user_role_organization_service: UserRoleOrganizationService = user_role_organization_service
) -> None:
    db_user_role_organization = await user_role_organization_service.get_user_role_organization_by_user_id_role_id(user_role_organization.user_id, user_role_organization.role_id)
    if not db_user_role_organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Role with id {user_role_organization.role_id} not assigned to user with id {user_role_organization.user_id}")
    await user_role_organization_service.delete_role_from_user(user_role_organization)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_role_organization_by_user_id(
    user_id: int,
    user_role_organization_service: UserRoleOrganizationService = user_role_organization_service
) -> None:
    db_user_role_organization = await user_role_organization_service.get_roles_by_user_id(user_id)
    if not db_user_role_organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    await user_role_organization_service.delete_user_role_organization_by_user_id(user_id)