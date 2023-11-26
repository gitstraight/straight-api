from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.models.organization import OrganizationResponse

class UserRequest(BaseModel):
    email: str
    password: str
    organization_id: int

class UserResponseBase(BaseModel):
    id: int
    email: str
    # password: str
    # created_at: datetime

class UserResponse(UserResponseBase):
    organization: OrganizationResponse

class UserByOrganizationResponse(BaseModel):
    organization: OrganizationResponse
    users: List[UserResponseBase]