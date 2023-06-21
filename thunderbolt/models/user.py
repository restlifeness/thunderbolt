
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash

from thunderbolt.core.settings import get_settings

from .base import ThunderboltModel


settings = get_settings()


class User(ThunderboltModel):
    """
    User model
    
    The User model represents a user of the application. This class includes
    """
    __tablename__ = 'user'
    
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    group_id = Column(UUID(as_uuid=True), ForeignKey('group.id'), nullable=True)
    admin_group_id = Column(UUID(as_uuid=True), ForeignKey('admin_group.id'), nullable=True)

    @property
    def password(self) -> str:
        """
        Get the password for the user.
        
        Raises:
            AttributeError: Password is not a readable attribute. Use `hashed_password` instead.
        """
        raise AttributeError("Password is not a readable attribute. Use `hashed_password` instead.")

    @password.setter
    def password(self, password: str) -> None:
        """
        Set the password for the user.
        
        Args:
            password (str): The password to be hashed and stored.
        """
        self.hashed_password = generate_password_hash(
            password,
            method=settings.HASH_METHOD,
            salt_length=settings.SALT_LENGTH
        )

    def check_password(self, password: str) -> bool:
        """
        Check the password for the user.
        
        Args:
            password (str): The password to be checked.
        """
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'<User {self.username}>'


"""
Integrations

Below, you will find models for various integrations. These models will inherit 
from the User model, and will be used as 'joined table inheritance' for extending 
and relating to the base User model. This design provides a way to add specific 
attributes or relationships to subsets of the base User model and facilitates data 
consistency and query efficiency.
"""


class TelegramIntegration(User):
    """
    TelegramIntegration model

    The TelegramIntegration model is a child class of the User model that represents 
    the integration of a user's Telegram account with our application. This class 
    includes unique Telegram identifiers and names, and it utilizes joined table 
    inheritance from the User model to extend and relate the user data.

    Attributes:
        telegram_username (str): The Telegram username of the user.
        telegram_id (int): The Telegram ID of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    # NOTE: This is an abstract class! For create table, use __tablename__ = 'telegram_integration'
    __abstract__ = True

    telegram_username = Column(String(255), unique=True, nullable=False)
    telegram_id = Column(Integer, unique=True, nullable=False)

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
