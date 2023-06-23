
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from thunderbolt.models import User
from thunderbolt.forum.repository.post import PostRepository
from thunderbolt.forum.service.post import PostService
from thunderbolt.forum.schema.post import PostInfoResponse, PostDataCreate, PostDataUpdate

from thunderbolt.users.dependencies import get_user_by_token


post_router = APIRouter(
    tags=["post", "forum"],
    prefix="/forum",
)


@post_router.get("/topics/threads/posts/users/{user_id}", response_model=list[PostInfoResponse])
async def get_all_posts_by_user(
    user_id: str,
    post_repo: Annotated[PostRepository, Depends(PostRepository)],
) -> list[PostInfoResponse]:
    """
    Get all posts by user.
    
    Args:
        user_id (str): The id of the user to be retrieved.
        post_repo (PostRepository): The post repository to be used.
    
    Returns:
        PostResponse: The requested post.
    """
    posts = await post_repo.get_by_user(user_id)
    return posts


@post_router.get("/topics/threads/{thread_id}/posts", response_model=list[PostInfoResponse])
async def get_all_posts_by_thread(
    thread_id: str,
    post_repo: Annotated[PostRepository, Depends(PostRepository)],
) -> list[PostInfoResponse]:
    """
    Get all posts by thread.
    
    Args:
        thread_id (str): The id of the thread to be retrieved.
        post_repo (PostRepository): The post repository to be used.
    
    Returns:
        PostResponse: The requested post.
    """
    posts = await post_repo.get_by_thread(thread_id)
    return posts


@post_router.get("/topics/threads/posts/{post_id}", response_model=PostInfoResponse)
async def get_post(
    post_id: str,
    post_repo: Annotated[PostRepository, Depends(PostRepository)],
) -> PostInfoResponse:
    """
    Get a post by id.
    
    Args:
        post_id (str): The id of the post to be retrieved.
        post_repo (PostRepository): The post repository to be used.
    
    Raises:
        HTTPException: If the requested post is not found.
    
    Returns:
        PostResponse: The requested post.
    """
    post = await post_repo.get(post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    return post


@post_router.post("/topics/threads/posts", response_model=PostInfoResponse)
async def create_post(
    post: PostDataCreate,
    user: Annotated[User, Depends(get_user_by_token)],
    post_service: Annotated[PostService, Depends(PostService)],
) -> PostInfoResponse:
    """
    Create a post.
    
    Args:
        thread_id (str): The id of the thread to be retrieved.
        post_repo (PostRepository): The post repository to be used.
    
    Returns:
        PostResponse: The requested post.
    """
    post = await post_service.create_post(user, post)
    return post


@post_router.put("/topics/threads/posts/{post_id}", response_model=PostInfoResponse)
async def update_post(
    post_data: PostDataUpdate,
    user: Annotated[User, Depends(get_user_by_token)],
    post_service: Annotated[PostService, Depends(PostService)],
) -> PostInfoResponse:
    """
    Update a post.
    
    Args:
        post_id (str): The id of the post to be retrieved.
        post_repo (PostRepository): The post repository to be used.
    
    Raises:
        HTTPException: If the requested post is not found.
    
    Returns:
        PostResponse: The requested post.
    """
    post = await post_service.update_post(user, post_data)
    return post


@post_router.delete("/topics/threads/posts/{post_id}", response_model=PostInfoResponse)
async def delete_post(
    post_id: str,
    user: Annotated[User, Depends(get_user_by_token)],
    post_service: Annotated[PostService, Depends(PostService)],
) -> PostInfoResponse:
    """
    Delete a post.
    
    Args:
        post_id (str): The id of the post to be retrieved.
        post_repo (PostRepository): The post repository to be used.
    
    Raises:
        HTTPException: If the requested post is not found.
    
    Returns:
        PostResponse: The requested post.
    """
    post = await post_service.delete_post(user, post_id)
    return post
