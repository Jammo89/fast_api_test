from typing import Annotated
from fastapi import Path, APIRouter


router = APIRouter(prefix="/items", tags=["Items"])
@router.get("/")
def items():
    return [{"items1": "11111"}, {"items2": "222222"}]


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item": {"id": item_id}}

