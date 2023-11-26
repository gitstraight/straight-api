from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.middleware.oauth2 import get_current_user
from app.core.services.organization_service import OrganizationService

from app.models.organization import OrganizationRequest, OrganizationResponse

router = APIRouter(
    prefix="/api/organizations", 
    tags=['Organization']
)

organization_service: OrganizationService = Depends(OrganizationService)

@router.get("", status_code=status.HTTP_200_OK, response_model=List[OrganizationResponse])
async def get_organizations(
    organization_service: OrganizationService = organization_service
) -> List[OrganizationResponse]:
    try:
        organizations = await organization_service.get_organizations()
        return organizations
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=OrganizationResponse)
async def get_organization_by_id(
    id: int, 
    organization_service: OrganizationService = organization_service
) -> OrganizationResponse:
    try:
        organization = await organization_service.get_organization_by_id(id)
        if not organization:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The organization with id {id} does not exist")
        return organization
    except Exception as e:
        raise e

@router.get("/name/{name}", status_code=status.HTTP_200_OK, response_model=OrganizationResponse)
async def get_organization_by_name(
    name: str, 
    organization_service: OrganizationService = organization_service
) -> OrganizationResponse:
    try:
        organization = await organization_service.get_organization_by_name(name)
        if not organization:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The organization with name '{name}' does not exist")
        return organization
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("", status_code=status.HTTP_201_CREATED, response_model=OrganizationResponse)
async def create_organization(
    new_organization: OrganizationRequest, 
    organization_service: OrganizationService = organization_service
) -> OrganizationResponse:
    try:
        organization_db = await organization_service.get_organization_by_name(new_organization.name)
        if organization_db:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"The organization with name '{new_organization.name}' already exists")
        organization = await organization_service.create_organization(new_organization)
        return organization
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_organization_by_id(
    id: int,
    organization_service: OrganizationService = organization_service
) -> None:
    try:
        organization = await organization_service.get_organization_by_id(id)
        if not organization:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The organization with id {id} does not exist")
        await organization_service.delete_organization_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_all_organizations(
    organization_service: OrganizationService = organization_service
) -> None:
    try:
        await organization_service.delete_all_organizations()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
