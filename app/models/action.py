from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.models.organization import OrganizationResponse
from app.models.user import UserResponse

class ActionRequest(BaseModel):
    name: str
    organization_id: int

class ActionResponseBase(BaseModel):
    id: int
    name: str
    # created_at: datetime

class ActionResponse(ActionResponseBase):
    organization: OrganizationResponse

class ActionsByOrganizationResponse(BaseModel):
    organization: OrganizationResponse
    actions: List[ActionResponseBase]

class ActionsByUserResponse(BaseModel):
    user: UserResponse
    actions: List[ActionResponseBase]