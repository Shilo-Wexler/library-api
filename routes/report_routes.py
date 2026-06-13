from fastapi import APIRouter

from logger import get_logger


logger = get_logger(__name__)
router = APIRouter()


@router.get('/summary')
def get_summary() -> dict:
    pass


@router.get('/books-by-genre')
def get_books_by_genre() -> dict:
    pass


@router.get('/top-member')
def get_top_borrows_member() -> dict:
    pass