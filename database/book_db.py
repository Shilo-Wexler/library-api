from mysql.connector import Error

from database.connection_db import sql_connection
from logger import get_logger


logger = get_logger(__name__)


class BookDB():    
    @staticmethod
    def add_new_book(data: dict) -> int:
        cursor = sql_connection.connection.cursor(dictionary=True)
        logger.info("Start adding a book")
        try:
            cursor.execute("""
                INSERT INTO books (title, author, genre)
                VALUES(%(title)s, %(author)s, %(genre)s)
                """, data
            )
            sql_connection.connection.commit()
            logger.info("The book was added successfully.")
            return cursor.lastrowid
        except Exception as e:
            logger.error("Error adding book: %s", e)
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    @staticmethod
    def get_all_books() -> list[dict]:
        cursor = sql_connection.connection.cursor(dictionary=True)
        logger.info("Start an attempt to return all books")
        try:
            cursor.execute("SELECT * FROM books")
            logger.info("The return of the books was successful.")
            return cursor.fetchall()
        except Exception as e:
            logger.error("Error in the book return process %s", e)
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    @staticmethod
    def get_book_by_id(id: int) -> dict:
        cursor = sql_connection.connection.cursor(dictionary=True)
        logger.info("Start an attempt to return book by id: %s", id)

        try:
            cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
            logger.info("The return of the book was successful.")
            return cursor.fetchone()
        except Exception as e:
            logger.error("Error finding book: %s", e)
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    @staticmethod
    def update_book_details(data: dict, id: int) -> bool:
        cursor = sql_connection.connection.cursor(dictionary=True)
        logger.info("Starting the book update operation")

        try:
            chenges = ','.join([f"{k} = %s" for k in data.keys()])
            values = tuple(data.values())
            query = f"UPDATE books SET {chenges} where id = %s"
            final_values = values + (id,)
            cursor.execute(query, final_values)
            sql_connection.connection.commit()
            if cursor.rowcount > 0:
                logger.info("Book updated successfully")
                return True
            logger.info("No update was performed.")
            return False
        except Exception as e:
            logger.error("No update was performed: %s", e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    @staticmethod
    def borrow_book(id: int, member_id: int) -> bool:
        pass



    @staticmethod
    def return_book(id: int, member_id: int) -> bool:
        pass
    
            


        




        



