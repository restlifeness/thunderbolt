
from pydantic import BaseModel, Field


class BearerToken(BaseModel):
    token: str = Field(description="The bearer token to be used for authorization")
    type: str = Field(description="The type of the token, should be 'bearer'", default="bearer")
