
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from thunderbolt.models import User
from thunderbolt.core.security import create_token, decode_token

from .repository import UserRepository
from .schema import BearerToken


class UserService:
    def __init__(
        self, 
        user_repository: Annotated[UserRepository, Depends()]
    ) -> None:
        self.user_repository: UserRepository = user_repository

    async def auth_user(self, user_data: OAuth2PasswordRequestForm) -> User:
        """
        Authenticate a user.

        Args:
            username (str): The username of the user to be authenticated.
            password (str): The password of the user to be authenticated.

        Returns:
            User: The authenticated user.
        """
        user = await self.user_repository.get_by_username(user_data.username)
        if not user:
            return False
        if not user.check_password(user_data.password):
            return False
        return user

    def create_token(self, user: User) -> str:
        """
        Create a JWT token for a user.

        Args:
            user (User): The user to create a token for.

        Returns:
            str: The JWT token.
        """
        payload = {"sub": str(user.id)}
        token = create_token(payload)
        return BearerToken(access_token=token, token_type="bearer")

    async def get_user_by_token(self, token: str) -> User:
        """
        Get a user by token.

        Args:
            token (str): The JWT token.

        Returns:
            User: The user.
        """
        payload = decode_token(token)
        username = payload.get("sub")
        user = await self.user_repository.get_by_username(username)
        return user