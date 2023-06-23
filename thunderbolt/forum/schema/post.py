
from pydantic import BaseModel, Field

from thunderbolt.forum.schema.thread import ThreadInfoWithRelatedResponse
from thunderbolt.users.schema import UserPersonalInfoResponse


class PostInfoResponse(BaseModel):
    id: int = Field(example=1, description='Post ID')
    thread: ThreadInfoWithRelatedResponse = Field(description='Thread')
    user: UserPersonalInfoResponse = Field(description='User')
    title: str = Field(example='Post title', description='Post title')

    class Config:
        orm_mode = True


class PostDataCreate(BaseModel):
    thread_id: int = Field(example=1, description='Thread ID')
    user_id: int = Field(example=1, description='User ID')
    title: str = Field(example='Post title', description='Post title')
    content: str = Field(example='Post content', description='Post content')


class PostDataUpdate(BaseModel):
    id: int = Field(example=1, description='Post ID')
    thread_id: int = Field(example=1, description='Thread ID')
    user_id: int = Field(example=1, description='User ID')
    title: str = Field(example='Post title', description='Post title')
    content: str = Field(example='Post content', description='Post content')
