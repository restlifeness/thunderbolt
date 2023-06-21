
from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/{user_id}")
async def get_user(user_id: str) -> None:
    pass


@router.post("/")
async def create_user() -> None:
    pass
