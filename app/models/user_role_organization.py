from pydantic import BaseModel

from app.models.role import RoleResponseBase
from app.models.user import UserResponseBase


class UserRoleOrganizationRequest(BaseModel):
    role_id: int
    user_id: int

class UserRoleOrganizationResponse(BaseModel):
    id: int
    role: RoleResponseBase
    user: UserResponseBase