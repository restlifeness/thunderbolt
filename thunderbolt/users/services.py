
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.exc import IntegrityError

from thunderbolt.models import User
from thunderbolt.core.security import create_token, decode_token

from .repository import UserRepository
from .schema import BearerToken, UserPersonalInfo


class UserService:
    """
    Service class for User model
    
    This class encapsulates the business logic for the User model. It provides
    functions for creating, updating and deleting user records.
    """
    ALLOWED_GENDERS = ('male', 'female', 'other')

    def __init__(
        self, 
        user_repository: Annotated[UserRepository, Depends(UserRepository)]
    ) -> None:
        self.user_repository: UserRepository = user_repository

    def _validate_gender(self, gender: str) -> None:
        """
        Validate user gender.
        
        Args:
            gender: user gender.
        
        Raises:
            HTTPException: Gender is not allowed
        """
        if gender and gender not in self.ALLOWED_GENDERS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Gender is not allowed"
            )

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

    def create_token(self, user: User) -> BearerToken:
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

    async def create_new_user(self, user_data: UserPersonalInfo) -> User:
        """
        Create a new user.

        Args:
            user_data (UserPersonalInfo): The user data.

        Raises:
            HTTPException: If the username already exists.
            HTTPException: If the email already exists.

        Returns:
            User: The created user.
        """
        self._validate_gender(user_data.gender)

        user = User(**user_data.dict())
        try:
            user = await self.user_repository(user)
        except IntegrityError as e:
            exception_string = str(e)
            if 'username' in exception_string:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists",
                )
            elif 'email' in exception_string:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists",
                )
        return user

    async def update_user(self, user: User, user_data: UserPersonalInfo) -> User:
        """
        Update a user.
        
        Args:
            user (User): The user to be updated.
            user_data (UserPersonalInfo): The user data.
        
        Returns:
            User: The updated user.
        """
        self._validate_gender(user_data.gender)
        
        user_dict = user_data.dict(exclude_unset=True)
        for field, value in user_dict.items():
            setattr(user, field, value)
        
        user = await self.user_repository.update(user)
        return user

    async def delete_user(self, user: User) -> None:
        await self.user_repository.delete(user)
