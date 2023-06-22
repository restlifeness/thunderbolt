
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from thunderbolt.users.schema import BearerToken
from thunderbolt.users.services import UserService


auth_router = APIRouter(
    tags=["auth"],
)


@auth_router.post("/token", response_model=BearerToken, status_code=status.HTTP_200_OK)
async def login(
    user_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: Annotated[UserService, Depends()],
) -> BearerToken:
    """
    OAuth2 compatible token login, get an access token for future requests
    
    Args:
        user_data (OAuth2PasswordRequestForm): The user data.
        user_service (UserService): The user service.

    Returns:
        BearerToken: The bearer token.
    """
    user = await user_service.auth_user(user_data)
    access_token = user_service.create_token(user)
    return access_token
