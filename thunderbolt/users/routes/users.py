import uuid

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from thunderbolt.models import User
from thunderbolt.users.dependencies import get_user_by_token
from thunderbolt.users.schema import UserPersonalInfo, UserPersonalInfoResponse
from thunderbolt.users.repository import UserRepository
from thunderbolt.users.services import UserService


user_router = APIRouter(
    tags=["user"],
)


@user_router.get("/users/{user_id}", response_model=UserPersonalInfoResponse)
async def get_user(
    user_id: str,
    user: Annotated[User, Depends(get_user_by_token)],
    user_repo: Annotated[UserRepository, Depends(UserRepository)],
) -> UserPersonalInfoResponse:
    """
    Get a user by id.
    
    Args:
        user_id (str): The id of the user to be retrieved.
        user (User): The user making the request.
        user_repo (UserRepository): The user repository to be used.
    
    Raises:
        HTTPException: If the user is not authorized to access the requested user.
        HTTPException: If the requested user is not found.
    
    Returns:
        UserPersonalInfoResponse: The requested user.
    """
    if user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user",
        )

    target_user = await user_repo.get(user_id)

    if not target_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return target_user

@user_router.put("/", response_model=UserPersonalInfoResponse)
async def create_user(
    user_data: UserPersonalInfo,
    user_service: Annotated[UserService, Depends(UserService)],
) -> UserPersonalInfoResponse:
    """
    Create a new user.
    
    Args:
        user_data (UserPersonalInfo): User data to be created.
        user_service (UserService): The user service to be used.
    
    Returns:
        UserPersonalInfoResponse: The created user.
    """
    return await user_service.create_new_user(user_data)


@user_router.post("/")
async def update_user(
    user_data: UserPersonalInfo,
    user: Annotated[User, Depends(get_user_by_token)],
    user_service: Annotated[UserService, Depends(UserService)],
) -> None:
    """
    Update a user.
    
    Args:
        user_data (UserPersonalInfo): User data to be updated.
        user (User): The user making the request.
        user_service: The user service to be used.

    Raises:
        HTTPException: If the user is not authorized to update the requested user.
    
    Returns:
        User: updated user.
    """
    return await user_service.update_user(user_data, user)


@user_router.delete("/{user_id}")
async def delete_user(
    user_id: str,
    user: Annotated[User, Depends(get_user_by_token)],
    user_repo: Annotated[UserRepository, Depends(UserRepository)],
) -> None:
    """
    Delete a user.
    
    Args:
        user_id (str): The id of the user to be deleted.
        user (User): The user making the request.
        user_repo (UserRepository): The user repository to be used.
    
    Raises:
        HTTPException: If the user is not authorized to delete the requested user.

    Returns:
        None
    """
    if user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user",
        )
    
    await user_repo.delete(user_id)
