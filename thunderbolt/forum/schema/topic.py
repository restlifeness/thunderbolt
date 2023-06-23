
from pydantic import BaseModel, Field


class TopicInfoResponse(BaseModel):
    symbol: str = Field(example='GEN', description='Topic symbol')
    title: str = Field(example='General', description='Topic title')
    description: str = Field(example='General discussion', description='Topic description')
