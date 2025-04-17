from users.schemas import CreateUser
from users import crud

from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
