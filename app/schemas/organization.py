
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.core.database.connector import Base
from sqlalchemy.orm import relationship


class Organizations(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True)
    api_key = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    
    roles = relationship("Roles", back_populates="organization")
    actions = relationship("Actions", back_populates="organization")
    users = relationship("Users", back_populates="organization")
   