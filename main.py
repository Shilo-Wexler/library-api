
from fastapi import FastAPI

from logger import get_logger
from routes import book_routes, member_routes, report_routes


logger = get_logger(__name__)

app = FastAPI()
app.include_router(book_routes.router, prefix='/books')
app.include_router(member_routes.router, prefix='/members')
app.include_router(report_routes.router, prefix='/reports')
