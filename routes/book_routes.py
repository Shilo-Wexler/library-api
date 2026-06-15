from fastapi import APIRouter, HTTPException

from logger import get_logger
from database.book_db import BookDB
from schemas import AddBook, UpdateBook, GetBook



router = APIRouter()
logger = get_logger(__name__)


@router.post('', status_code=201)
def add_book(body: AddBook) -> int:
    try:
        new_book = body.model_dump()
        return BookDB.add_new_book(new_book)
    except Exception as e:
        raise HTTPException(status_code=422, detail="Email already exists in the system.")        


@router.get('')
def get_books() -> list[GetBook]:
    all_books = BookDB.get_all_books()
    if all_books:
        return [GetBook(**b) for b in all_books]
    else:
        logger.info("No books found")
        raise HTTPException(status_code=404, detail="No books found")


@router.get('/{id}')
def get_book(id: int) -> GetBook:
    book = BookDB.get_book_by_id(id)
    if book:
        return GetBook(**book)
    else:
        logger.info("Book does not exist.")
        raise HTTPException(status_code=404, detail="Book does not exist.")


@router.patch('/{id}')
def update_book(id: int, body: UpdateBook) -> bool:
    changes = body.model_dump(exclude_unset=True)
    return BookDB.update_book_details(changes, id)


@router.patch('/{id}/borrow/{member_id}')
def borrow_book(id: int, member_id: int) -> bool:
    try:
        borrow_status =  BookDB.borrow_book(id, member_id)
        if not borrow_status:
            raise HTTPException(status_code=404, detail="book not found")
        return True
    except ValueError:
        raise HTTPException(status_code=422, detail="it is already borrowed.")
    except Exception as e:
        raise HTTPException(status_code=422)


@router.patch('/{id}/return/{member_id}')
def return_book(id: int, member_id: int) -> bool:
    try:
        return_status = BookDB.return_book(id, member_id)
        if not return_status:
            raise HTTPException(status_code=404, detail="book not found")
        return True
    except Exception as e:
        raise HTTPException(status_code=422)