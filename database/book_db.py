from mysql.connector import Error

from database.connection_db import sql_connection
from logger import get_logger


logger = get_logger(__name__)


class BookDB:    
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
        logger.info("Starting the book borrowing process")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            if BookDB.count_active_borrows_by_member(member_id) >=7:
                raise IndexError("You have already borrowed 7 books.")
            cursor.execute("""
                UPDATE books SET is_available = FALSE, borrowed_by_member_id = %s
                WHERE id = %s AND is_available = TRUE""", (member_id, id))
            if not cursor.rowcount > 0:
                raise ValueError("it is already borrowed.")
            cursor.execute("UPDATE members SET total_borrows = total_borrows + 1 WHERE id = %s", (member_id,))
            sql_connection.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    @staticmethod
    def count_active_borrows_by_member(member_id) -> int:
        logger.info("Starting to count books borrowing by member process")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("""SELECT COUNT(*) AS amount_of_books 
                FROM books WHERE borrowed_by_member_id = %s""", (member_id,))
            result = cursor.fetchone()
            return result['amount_of_books']
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    



    @staticmethod
    def return_book(id: int, member_id: int) -> bool:
        logger.info("Starting the book returning process")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("""
                UPDATE books SET is_available = TRUE, borrowed_by_member_id = NULL 
                WHERE id = %s AND is_available = FALSE AND borrowed_by_member_id = %s
            """, (id, member_id)
            )
            sql_connection.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")

    

    @staticmethod
    def count_total_books() -> int:
        logger.info("Starting the book counting process")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT COUNT(*) AS amount_of_books FROM books")
            result = cursor.fetchone()
            logger.info("Quantity counting completed")
            return result['amount_of_books']
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")


    @staticmethod
    def count_books_by_status(is_available: bool) -> int:
        logger.info("Starting the book counting process")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT COUNT(*) AS amount_of_books FROM books WHERE is_available = %s", (is_available,))
            result = cursor.fetchone()
            logger.info("Quantity counting completed")
            return result['amount_of_books']
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    def count_by_genre() -> dict:
        logger.info("Starting the book counting  by genre process")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT genre, COUNT(*) as amount_of_books FROM books GROUP BY genre")
            return cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")

        




        



