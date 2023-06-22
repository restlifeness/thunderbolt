
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from thunderbolt.models import User
from thunderbolt.users.dependencies import get_user_by_token


router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@router.get("/{user_id}")
async def get_user(
    user_id: str,
    user: Annotated[User, Depends(get_user_by_token)]
) -> None:
    pass


@router.put("/")
async def create_user() -> None:
    pass


@router.post("/")
async def update_user() -> None:
    pass


@router.delete("/")
async def delete_user() -> None:
    pass
