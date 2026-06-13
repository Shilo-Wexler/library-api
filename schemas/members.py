from pydantic import BaseModel, EmailStr


class BaseMember(BaseModel):
    name: str
    email: EmailStr


class CreateMember(BaseMember):
    pass


class GetMember(BaseMember):
    id: int
    is_active: bool
    total_borrows: int


class UpdateMember(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
