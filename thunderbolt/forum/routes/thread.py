
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

# TODO: add __init__ files to all folders
from thunderbolt.forum.repository.thread import ThreadRepository
from thunderbolt.forum.schema.thread import ThreadInfoWithRelatedResponse


thread_router = APIRouter(
    tags=["thread", "forum"],
    prefix="/forum",
)


@thread_router.get("/threads", response_model=list[ThreadInfoWithRelatedResponse])
async def get_all_threads(
    thread_repo: Annotated[ThreadRepository, Depends(ThreadRepository)],
) -> list[ThreadInfoWithRelatedResponse]:
    """
    Get all threads.
    
    Args:
        thread_repo (ThreadRepository): The thread repository to be used.
    
    Returns:
        ThreadResponse: The requested thread.
    """
    threads = await thread_repo.get_all()
    return threads


@thread_router.get("/threads/{thread_id}", response_model=ThreadInfoWithRelatedResponse)
async def get_thread(
    thread_id: str,
    thread_repo: Annotated[ThreadRepository, Depends(ThreadRepository)],
) -> ThreadInfoWithRelatedResponse:
    """
    Get a thread by id.
    
    Args:
        thread_id (str): The id of the thread to be retrieved.
        thread_repo (ThreadRepository): The thread repository to be used.
    
    Raises:
        HTTPException: If the requested thread is not found.
    
    Returns:
        ThreadResponse: The requested thread.
    """
    thread = await thread_repo.get(thread_id)

    if not thread:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thread not found",
        )

    return thread
