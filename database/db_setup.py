import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from queries import CREATE_BOOKS_TABLE, CREATE_MEMBERS_TABLE
from connection_db import get_connection
from logger import get_logger

logger = get_logger(__name__)


def create_table(create_table_command: str) -> None:
    """
    The function receives a command to create a table in SQL format,
    opens a connection and executes the command.

    Args:
        create_table_command: SQL command
    """
    connection = None
    cursor = None

    logger.info("Starting to create the table")

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(create_table_command)
        logger.info("The table was created successfully.")
    except Exception as e:
        logger.error("Table creation failed: %s", e)
        raise

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        logger.info("Connections closed")


def setup_books_members_tables () -> None:
    """
    Initialize the tables in the order of their relationships
    """
    logger.info("Submitting the create command for a member table")
    create_table(CREATE_MEMBERS_TABLE)
    logger.info("Submitting the create command for the books table")
    create_table(CREATE_BOOKS_TABLE)
    logger.info("The tables were created successfully.")

