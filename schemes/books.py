from enum import Enum
from pydantic import BaseModel


class Genre(str, Enum):
    fiction = 'Fiction' 
    non_fiction = 'Non-Fiction'
    science = 'Science'
    history = 'History'
    other = 'Other'


class BaseBook(BaseModel):
    title: str
    author: str
    genre: Genre


class AddBook(BaseBook):
    pass


class GetBook(BaseBook):
    id: int
    is_available: bool
    borrowed_by_member_id: int | None


class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    genre: Genre | None = None