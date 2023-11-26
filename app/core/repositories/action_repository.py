from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.repositories.interfaces.action_repository_interface import ActionRepositoryInterface
from app.models.action import ActionRequest
from app.schemas.action import Actions

from app.core.database.connector import get_db
from app.schemas.role import Roles
from app.schemas.user_role_organization import UserRoleOrganization
from app.schemas.rule import Rules
from app.schemas.user import Users


class ActionRepository(ActionRepositoryInterface):

    def __init__(
        self,
        db: Session = Depends(get_db)
    ):
        self.db = db
    
    async def get_action_by_id(
        self,
        id: int
    ):
        action = self.db.query(Actions).filter(Actions.id == id).first()
        return action

    async def get_actions_by_user_id(
        self,
        user_id: int
    ):
        actions = (
            self.db
            .query(Actions)
            .join(Rules)
            .join(Roles)
            .filter(Roles.id == UserRoleOrganization.role_id)
            .filter(UserRoleOrganization.user_id == user_id)
            # .join(RolesUsers)
            # .join(Users)
            # .filter(Users.id == user_id)
            .all()
        )
        return actions

    async def get_actions_by_organization_id(
        self,
        organization_id: int
    ):
        actions = self.db.query(Actions).filter(Actions.organization_id == organization_id).all()
        return actions

    async def get_action_by_name_organization_id(
        self,
        name: str,
        organization_id: int
    ):
        action = self.db.query(Actions).filter(Actions.name == name, Actions.organization_id == organization_id).first()
        return action
    
    async def create_action(
        self,
        action: ActionRequest
    ):
        new_action = Actions(**action.model_dump())
        self.db.add(new_action)
        self.db.commit()
        self.db.refresh(new_action)
        return new_action
    
    async def delete_action_by_id(
        self,
        id: int
    ):
        action = self.db.query(Actions).filter(Actions.id == id).first()
        self.db.delete(action)
        self.db.commit()

    async def delete_actions_by_organization_id(
        self,
        organization_id: int
    ):
        actions = self.db.query(Actions).filter(Actions.organization_id == organization_id).all()
        for action in actions:
            self.db.delete(action)
        self.db.commit()
            