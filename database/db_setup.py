import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.queries import CREATE_BOOKS_TABLE, CREATE_MEMBERS_TABLE
from database.connection_db import sql_connection
from logger import get_logger

logger = get_logger(__name__)


def setup_books_members_tables() -> None:
    """
    Initialize the tables in the order of their relationships
    """
    connection = None
    cursor = None

    logger.info("Starting to create the tables")

    try:
        cursor =  sql_connection.connection.cursor()

        logger.info("Submitting the create command for a member table")
        cursor.execute(CREATE_MEMBERS_TABLE)
        logger.info("The members table was created successfully.")
        logger.info("Submitting the create command for the books table")
        cursor.execute(CREATE_BOOKS_TABLE)
        logger.info("The books table was created successfully.")

        sql_connection.connection.commit()

    except Exception as e:
        logger.error("Table creation failed: %s", e)
        raise

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        logger.info("Connections closed")

        