from typing import List
from pydantic import BaseModel
from datetime import datetime

class OrganizationRequest(BaseModel):
    name: str

class OrganizationResponse(BaseModel):
    id: int
    name: str
    # api_key: str
    # created_at: datetime

