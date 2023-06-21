
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from thunderbolt.user.schema import BearerToken
from thunderbolt.user.services import UserService
from thunderbolt.core.security import dec


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.post("/token", response_model=BearerToken, status_code=status.HTTP_200_OK)
async def login(
    user_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: Annotated[UserService, Depends()],
) -> None:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await user_service.auth_user(user_data)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = user_service.create_token(user)

    return access_token