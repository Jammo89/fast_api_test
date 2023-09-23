from fastapi import APIRouter
from users.shemas import CreateUser
from users.crud import create_users


router = APIRouter(prefix="/users", tags=["Users"])



@router.post("/")
def create_user(user: CreateUser):
    return create_users(user_in=user)
