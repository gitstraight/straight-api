from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.models.organization import OrganizationResponse

class RoleRequest(BaseModel):
    name: str
    organization_id: int

class RoleResponseBase(BaseModel):
    id: int
    name: str
    # created_at: datetime

class RoleResponse(RoleResponseBase):
    organization: OrganizationResponse

class RolesByOrganizationResponse(BaseModel):
    organization: OrganizationResponse
    roles: List[RoleResponseBase]