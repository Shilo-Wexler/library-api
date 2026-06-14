from database.connection_db import sqlConnection
from logger import get_logger


logger = get_logger(__name__)


class BookDB():    
        @staticmethod
        def create_book(data: dict) -> dict:
            cur = sqlConnection.conn.cursor(dictionary=True)
            logger.info("Start adding a book")
