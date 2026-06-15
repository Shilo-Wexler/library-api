from fastapi import APIRouter

from database.member_db import MemberDB
from database.book_db import BookDB

from logger import get_logger


logger = get_logger(__name__)
router = APIRouter()


@router.get('/summary')
def get_summary() -> dict:
    return {
        "total_books": BookDB.count_total_books(),
        "available_books": BookDB.count_books_by_status(True),
        "currently_borrowed":  BookDB.count_books_by_status(False),
        "active_member": MemberDB.count_active_members()
    }


@router.get('/books-by-genre')
def get_books_by_genre() -> list:
    return BookDB.count_by_genre()


@router.get('/top-member')
def get_top_borrows_member() -> dict:
    return MemberDB.get_top_member()