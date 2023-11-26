from app.schemas.organization import Base as OrganizationsBase
from app.schemas.user import Base as UsersBase
from app.schemas.role import Base as RolesBase
from app.schemas.action import Base as ActionsBase
from app.schemas.user_role_organization import Base as RolesUsersBase
from app.schemas.rule import Base as RulesBase


Base = [UsersBase, RolesBase, ActionsBase, RolesUsersBase, OrganizationsBase, RulesBase]


