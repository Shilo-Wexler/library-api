import sys
import uvicorn
from fastapi import FastAPI

from logger import get_logger
from database import db_setup
from routes import book_routes, member_routes, report_routes


logger = get_logger(__name__)

app = FastAPI(
    title="Management API",
    description="User book and report management system"
)

app.include_router(book_routes.router, 
    prefix='/books', tags=["Books"]
)
app.include_router(member_routes.router,
    prefix='/members', tags=["Members"]
)
app.include_router(report_routes.router,
    prefix='/reports', tags=["Reports"]
)



if __name__ == '__main__':
    try:
        db_setup.setup_books_members_tables()
    except Exception as e:
        logger.critical("Table creation failure: %s", e)
    try:
        uvicorn.run('main:app', reload=True)
    except Exception as e:
        logger.critical("app failed to start: %s", e)
        sys.exit(1)

