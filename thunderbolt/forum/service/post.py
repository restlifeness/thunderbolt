
from typing import Annotated
from fastapi import Depends, HTTPException, status

from thunderbolt.models import User, Post

from thunderbolt.forum.schema.post import PostDataCreate, PostInfoResponse
from thunderbolt.forum.repository.post import PostRepository


class PostService:
    """
    Service for post related operations.
    """

    def __init__(
        self, 
        post_repo: Annotated[PostRepository, Depends(PostRepository)]
    ) -> None:
        self.post_repo: PostRepository = post_repo

    async def create_post(self, user: User, post_data: PostDataCreate) -> Post:
        """
        Create a post.

        Args:
            user (User): The user making the request.
            post_data (PostDataCreate): The post data to be used.

        Raises:
            HTTPException: If the requested thread is not found.

        Returns:
            Post: The created post.
        """
        post_data_dict = post_data.dict()
        post_model = Post()
        
        for field, value in post_data_dict.items():
            setattr(post_model, field, value)
        
        post_model.user_id = user.id
        
        post = await self.post_repo.add(post_model)
        return post

    async def update_post(self, user: User, post_data: PostDataCreate) -> Post:
        """
        Update a post.

        Args:
            user (User): The user making the request.
            post_data (PostDataCreate): The post data to be used.

        Raises:
            HTTPException: If the requested thread is not found.

        Returns:
            Post: The created post.
        """
        post_data_dict = post_data.dict()
        post_model = Post()
        
        for field, value in post_data_dict.items():
            setattr(post_model, field, value)
        
        post_model.user_id = user.id
        
        post = await self.post_repo.update(post_model)
        return post

    async def delete_post(self, user: User, post_id: str) -> None:
        """
        Delete a post.

        Args:
            user (User): The user making the request.
            post_id (str): The id of the post to be deleted.

        Raises:
            HTTPException: If the requested post is not found.
        """
        post = await self.post_repo.get(post_id)

        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found",
            )

        if post.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User is not authorized to delete this post",
            )

        await self.post_repo.delete(post)
