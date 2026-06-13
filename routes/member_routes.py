from fastapi import APIRouter

from logger import get_logger
from schemas import CreateMember, UpdateMember, GetMember


logger = get_logger(__name__)
router = APIRouter()


@router.post('', status_code=201)
def add_member(body: CreateMember) -> GetMember:
    pass


@router.get('')
def get_members() -> list[GetMember]:
    pass


@router.get('/{id}')
def get_member(id: int) -> GetMember:
    pass


@router.patch('/{id}')
def update_member(id: int, body: UpdateMember) -> GetMember:
    pass


@router.patch('/{id}/deactivate')
def deactivate_member(id: int) -> GetMember:
    pass


@router.patch('/{id}/activate')
def activate_member(id: int) -> GetMember:
    pass
