import mysql.connector

import logger


logger = logger.get_logger(__name__)


def get_connection() -> mysql.connector.MySQLConnection:
    """
    Establishes a connection to the database.

    Returns: 
        MySQLConnection: An active connection to the database.
    """
    logger.info("Starting an attempt to establish a connection to the database")
    try:
        return mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='secret',
            database='library_db',
            charset='utf8mb4'
        )
    except Exception as e:
        logger.error(e)
        raise
    
