from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app.core.services.organization_service import OrganizationService
from app.core.services.role_service import RoleService

from app.models.role import RoleRequest, RoleResponse, RolesByOrganizationResponse

router = APIRouter(
    prefix="/api/roles",
    tags=['Roles']
)

role_service: RoleService = Depends(RoleService)
organization_service: OrganizationService = Depends(OrganizationService)

@router.get("/{organization_id}", status_code=status.HTTP_200_OK, response_model=RolesByOrganizationResponse)
async def get_roles_by_organization_id(
    organization_id: int,
    role_service: RoleService = role_service,
    organization_service: OrganizationService = organization_service
) -> RolesByOrganizationResponse:
    organization = await organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    roles = await role_service.get_roles_by_organization_id(organization_id)
    return {'organization': organization, 'roles': roles}

@router.post("", status_code=status.HTTP_201_CREATED, response_model=RoleResponse)
async def create_role(
    new_role: RoleRequest,
    role_service: RoleService = role_service,
    organization_service: OrganizationService = organization_service
) -> RoleResponse:
    organization = await organization_service.get_organization_by_id(new_role.organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    db_role = await role_service.get_role_by_name_organization_id(new_role.name, new_role.organization_id)
    if db_role:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Role already exists")
    role = await role_service.create_role(new_role)
    return role

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_role_by_id(
    id: int,
    role_service: RoleService = role_service,
) -> None:
    role = await role_service.get_role_by_id(id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    await role_service.delete_role_by_id(id)

@router.delete("/organization/{organization_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_roles_by_organization_id(
    organization_id: int,
    role_service: RoleService = role_service,
    organization_service: OrganizationService = organization_service
) -> None:
    organization = await organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    await role_service.delete_roles_by_organization_id(organization_id)