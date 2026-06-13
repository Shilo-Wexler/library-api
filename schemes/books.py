from enum import Enum
from pydantic import BaseModel


class Genre(str, Enum):
    fiction = 'Fiction' 
    non_fiction = 'Non-Fiction'
    science = 'Science'
    history = 'History'
    other = 'Other'


class AddBook(BaseModel):
    title: str
    author: str
    genre: Genre


class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    genre: Genre | None = None


