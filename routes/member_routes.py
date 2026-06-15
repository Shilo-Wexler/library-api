from fastapi import APIRouter, HTTPException
from mysql.connector import IntegrityError

from logger import get_logger
from database.member_db import MemberDB
from schemas import CreateMember, UpdateMember, GetMember


logger = get_logger(__name__)
router = APIRouter()


@router.post('', status_code=201)
def add_member(body: CreateMember) -> int:
    new_member = body.model_dump()
    try:
        return MemberDB.add_new_member(new_member)
    except IntegrityError as e:
        logger.error("email already exists: %s", e)
        raise HTTPException(status_code=409, detail="The email already exists in the system.")


@router.get('')
def get_members() -> list[GetMember]:
    all_members = MemberDB.get_all_members()
    if all_members:
        return [GetMember(**m) for m in all_members]
    raise HTTPException(status_code=404, detail="The members does not exist.")


@router.get('/{id}')
def get_member(id: int) -> GetMember:
    member = MemberDB.get_member_by_id(id)
    if member:
        return GetMember(**member)
    raise HTTPException(status_code=404, detail="The member does not exist.")


@router.patch('/{id}')
def update_member(id: int, body: UpdateMember) -> bool:
    changes = body.model_dump(exclude_unset=True)
    try:
        return MemberDB.update_member_detailes(changes, id)
    except IntegrityError as e:
        logger.error("email already exists: %s", e)
        raise HTTPException(status_code=409, detail="The email already exists in the system.")



@router.patch('/{id}/deactivate')
def deactivate_member(id: int) -> bool:
    is_update =  MemberDB.update_status(id, False)
    if not is_update:
        raise HTTPException(status_code=404, detail="The member does not exist.")
    return True


@router.patch('/{id}/activate')
def activate_member(id: int) -> bool:
    is_update =  MemberDB.update_status(id, True)
    if not is_update:
        raise HTTPException(status_code=404, detail="The member does not exist.")
    return True
