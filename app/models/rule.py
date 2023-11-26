from datetime import datetime
from typing import List
from pydantic import BaseModel
from app.models.action import ActionResponseBase
from app.models.organization import OrganizationResponse
from app.models.role import RoleResponseBase


class RuleRequest(BaseModel):
    action_id: int
    role_id: int

class RuleResponseBase(BaseModel):
    id: int
    role: RoleResponseBase
    action: ActionResponseBase
    # created_at: datetime

class RuleResponse(RuleResponseBase):
    organization: OrganizationResponse

class RulesByOrganizationResponse(BaseModel):
    organization: OrganizationResponse
    rules: List[RuleResponseBase]

