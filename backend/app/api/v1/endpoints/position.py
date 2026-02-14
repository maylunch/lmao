from fastapi import APIRouter
from ...schemas.portfolio import PositionCreate

router = APIRouter()

@router.post("")
def add_position(payload: PositionCreate):
    return {"status": "ok"}

@router.put("/{id}")
def update_position(id: int):
    return {"status": "ok"}

@router.delete("/{id}")
def delete_position(id: int):
    return {"status": "ok"}