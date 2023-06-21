
from sqlalchemy import *
from sqlalchemy.orm import relationship

from .base import ThunderboltModel


class Group(ThunderboltModel):
    """
    Group model
    
    The Group model represents a group that a user can be a member of.
    
    """
    __tablename__ = 'group'

    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    users = relationship('User', secondary='group_user')

    def __repr__(self):
        return f'<Group {self.name}>'


class AdminGroup(ThunderboltModel):
    """
    AdminGroup model
    
    The AdminGroup model represents a group that a user can be an admin of.
    
    """
    __tablename__ = 'admin_group'

    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    admins = relationship('User', secondary='admin_group_user')

    def __repr__(self):
        return f'<AdminGroup {self.name}>'
