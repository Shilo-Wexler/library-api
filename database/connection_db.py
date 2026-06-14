import mysql.connector

import logger


logger = logger.get_logger(__name__)

    
class SqlConnection:
    def __init__(self):
        self.connection = self._connect()

    def _connect(self) -> mysql.connector.MySQLConnection:
        """
        Establishes a connection to the database.
    
class SqlConnection:
    def __init__(self):
        self.connection = self._connect()

    def _connect(self) -> mysql.connector.MySQLConnection:
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


sql_connection = SqlConnection()