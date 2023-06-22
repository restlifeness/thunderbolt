
from typing import Optional
from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field



class BearerToken(BaseModel):
    token: str = Field(description="The bearer token to be used for authorization")
    type: str = Field(description="The type of the token, should be 'bearer'", default="bearer")


class UserPersonalInfo(BaseModel):
    username: str = Field(description="The username of the user")
    email: str = Field(description="The email of the user")
    name: str = Field(description="The name of the user")
    description: Optional[str] = Field(description="The description of the user", default=None)
    gender: Optional[str] = Field(description="Gender of the user", default="other")
    birthday: Optional[date] = Field(description="Birthday of the user", default=None)


class UserPersonalInfoResponse(UserPersonalInfo):
    id: UUID = Field(description="The uuid of the user")

