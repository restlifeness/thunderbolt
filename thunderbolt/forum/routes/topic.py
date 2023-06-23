
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

# TODO: add __init__ files to all folders
from thunderbolt.forum.repository.topic import TopicRepository
from thunderbolt.forum.schema.topic import TopicInfoResponse


topic_router = APIRouter(
    tags=["topic", "forum"],
    prefix="/forum",
)


@topic_router.get("/topics", response_model=list[TopicInfoResponse])
async def get_all_topics(
    topic_repo: Annotated[TopicRepository, Depends(TopicRepository)],
) -> list[TopicInfoResponse]:
    """
    Get all topics.
    
    Args:
        topic_repo (TopicRepository): The topic repository to be used.
    
    Returns:
        TopicResponse: The requested topic.
    """
    topics = await topic_repo.get_all()
    return topics


@topic_router.get("/topics/{topic_id}", response_model=TopicInfoResponse)
async def get_topic(
    topic_id: str,
    topic_repo: Annotated[TopicRepository, Depends(TopicRepository)],
) -> TopicInfoResponse:
    """
    Get a topic by id.
    
    Args:
        topic_id (str): The id of the topic to be retrieved.
        topic_repo (TopicRepository): The topic repository to be used.
    
    Raises:
        HTTPException: If the requested topic is not found.
    
    Returns:
        TopicResponse: The requested topic.
    """
    topic = await topic_repo.get(topic_id)

    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Topic not found",
        )

    return topic
