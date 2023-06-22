
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from thunderbolt.models import User

from .services import UserService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user_by_token(
    token: Annotated[OAuth2PasswordBearer, Depends()],
    user_service: Annotated[UserService, Depends()]
) -> User:
    """
    Get a user by token.

    Args:
        token (str): The JWT token.
        user_service (UserService): The user service.

    Returns:
        User: The user.
    """
    user = await user_service.get_user_by_token(token)
    return user
