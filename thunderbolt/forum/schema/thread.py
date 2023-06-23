
from pydantic import BaseModel, Field

from thunderbolt.forum.schema.topic import TopicInfoResponse


class ThreadInfoWithoutRelatedResponse(BaseModel):
    title: str = Field(
        example='Hello world',
        description='Thread title'
    )
    description: str = Field(
        example='Hello world',
        description='Thread description'
    )


class ThreadInfoWithRelatedResponse(ThreadInfoWithoutRelatedResponse):
    topic: TopicInfoResponse = Field(
        example=TopicInfoResponse(
            symbol='GEN', 
            title='General', 
            description='General discussion'
        ), 
        description='Topic'
    )
