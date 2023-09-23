from typing import Annotated
from annotated_types import MaxLen, MinLen

from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    # usersname: str = Field(..., max_length=3, MaxLen=30)
    users_name: Annotated[str, MinLen(4), MaxLen(40)]
    email: EmailStr



