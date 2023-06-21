
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from thunderbolt.models import User

from .services import UserService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user_by_token(
    token: Annotated[OAuth2PasswordBearer, Depends()],
    user_service: Annotated[UserService, Depends()]
) -> User:
    user = await user_service.get_user_by_token(token)
    return user
