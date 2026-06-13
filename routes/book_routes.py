from fastapi import APIRouter

from logger import get_logger
from schemas import AddBook, UpdateBook, GetBook


router = APIRouter()
logger = get_logger(__name__)


@router.post('', status_code=201)
def add_book(body: AddBook) -> GetBook:
    pass


@router.get('')
def get_books() -> list[GetBook]:
    pass


@router.get('/{id}')
def get_book(id: int) -> GetBook:
    pass


@router.patch('/{id}')
def update_book(id: int, body: UpdateBook) -> GetBook:
    pass


@router.patch('/{id}/borrow/{member_id}')
def borrow_book(id: int, member_id: int) -> GetBook:
    pass


@router.patch('/{id}/return/{member_id}')
def return_book(id: int, member_id: int) -> GetBook:
    pass