from database.connection_db import sql_connection
from logger import get_logger


logger = get_logger(__name__)


class MemberDB:
    @staticmethod
    def add_new_member(data: dict) -> int:
        logger.info("Starting the process of creating a member")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute( "INSERT INTO members(name, email) VALUES (%(name)s, %(email)s)", data)
            sql_connection.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            logger.error("Adding a member failed: ", )
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    


    @staticmethod
    def get_all_members() -> list[dict]:
        logger.info("Starting the process of getting all memberes")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM members")
            return cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")
    

    @staticmethod
    def get_member_by_id(id) -> dict:
        logger.info("Starting the process of getting membere")
        cursor = sql_connection.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM members WHERE id = %s", (id,))
            return cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")

    
    @staticmethod
    def update_member_detailes(data: dict, id: int) -> bool:
        logger.info("Starting the process of updating membere")
        cursor = sql_connection.connection.cursor(dictionary=True)
        
        keys = ",".join([f"{k} = %s" for k in data.keys()])
        values = tuple(data.values()) + (id,)
        query = F"UPDATE members SET {keys} WHERE id = %s"

        try:
            cursor.execute(query, values)
            sql_connection.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")

    
    @staticmethod
    def update_status(id: int, status: bool) -> bool:
        logger.info("Starting the process of updating membere status")
        cursor = sql_connection.connection.cursor(dictionary=True)

        try:
            cursor.execute("UPDATE members SET is_active = %s WHERE id = %s", (status, id))
            sql_connection.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            logger.error(e)
            raise
        finally:
            cursor.close()
            logger.info("Closing the cursor connection")



    


