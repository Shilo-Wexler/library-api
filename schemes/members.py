from pydantic import BaseModel


class CreateMember(BaseModel):
    name: str
    email: str


class UpdateMember(BaseModel):
    name: str | None = None
    email: str | None = None
