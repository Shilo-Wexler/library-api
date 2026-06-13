from fastapi import APIRouter

from logger import get_logger
from schemas import CreateMember, UpdateMember, GetMember


logger = get_logger(__name__)
router = APIRouter()


@router.post('/members', status_code=201)
def add_member(body: CreateMember) -> GetMember:
    pass


@router.get('/members')
def get_members() -> list[GetMember]:
    pass


@router.get('/members/{id}')
def get_member(id: int) -> GetMember:
    pass


@router.patch('/members/{id}')
def update_member(id: int, body: UpdateMember) -> GetMember:
    pass


@router.patch('/members/{id}/deactivate')
def deactivate_member(id: int) -> GetMember:
    pass


@router.patch('/members/{id}/activate')
def activate_member(id: int) -> GetMember:
    pass
