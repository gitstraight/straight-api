from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.services.action_service import ActionService
from app.core.services.organization_service import OrganizationService
from app.core.services.role_service import RoleService

from app.core.services.rule_service import RuleService
from app.models.rule import RuleRequest, RuleResponseBase, RulesByOrganizationResponse


router = APIRouter(
    prefix="/api/rules",
    tags=['Rules']
)

rule_service: RuleService = Depends(RuleService)
organization_service: OrganizationService = Depends(OrganizationService)
action_service: ActionService = Depends(ActionService)
role_service: RoleService = Depends(RoleService)

@router.get("/{organization_id}", status_code=status.HTTP_200_OK, response_model=RulesByOrganizationResponse)
async def get_rules_by_organization_id(
    organization_id: int,
    rule_service: RuleService = rule_service,
    organization_service: OrganizationService = organization_service
) -> RulesByOrganizationResponse:
    organization = await organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    rules = await rule_service.get_rules_by_organization_id(organization_id)
    return {'organization': organization, 'rules': rules}

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RuleResponseBase)
async def create_rule(
    new_rule: RuleRequest,
    rule_service: RuleService = rule_service,
    action_service: ActionService = action_service,
    role_service: RoleService = role_service
) -> RuleResponseBase:
    action = await action_service.get_action_by_id(new_rule.action_id)
    if not action:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")
    role = await role_service.get_role_by_id(new_rule.role_id)
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    if action.organization.id != role.organization.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Action and Role must belong to the same organization")
    db_rule = await rule_service.get_rule_by_action_id_and_role_id(new_rule.action_id, new_rule.role_id)
    if db_rule:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rule already exists")
    rule = await rule_service.create_rule(new_rule)
    return rule

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rule_by_id(
    id: int,
    rule_service: RuleService = rule_service
) -> None:
    rule = await rule_service.get_rule_by_id(id)
    if not rule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rule not found")
    await rule_service.delete_rule_by_id(id)

@router.delete("/organization/{organization_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rules_by_organization_id(
    organization_id: int,
    rule_service: RuleService = rule_service,
    organization_service: OrganizationService = organization_service
) -> None:
    organization = await organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
    await rule_service.delete_rules_by_organization_id(organization_id)