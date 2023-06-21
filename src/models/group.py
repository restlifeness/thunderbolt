
from sqlalchemy import *
from sqlalchemy.orm import relationship

from .base import ThunderboltModel


class Group(ThunderboltModel):
    __tablename__ = 'group'

    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    users = relationship('User', secondary='group_user')

    def __repr__(self):
        return f'<Group {self.name}>'


class AdminGroup(ThunderboltModel):
    __tablename__ = 'admin_group'

    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    admins = relationship('User', secondary='admin_group_user')

    def __repr__(self):
        return f'<AdminGroup {self.name}>'
