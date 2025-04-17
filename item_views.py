from fastapi import Path, APIRouter
from typing import Annotated

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    return [
        "item1",
        "item2",
        "item3",
    ]


@router.get("/latest/")
def latest_item():
    return {
        "latest": {
            "id": "arbuzblyat",
        },
    }


@router.get("/{itemid}")
def item_id(itemid: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            itemid: "bombardirocrocadilo",
        },
    }
