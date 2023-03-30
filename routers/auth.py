from fastapi import APIRouter

from config.database import SessionLocal
from schemas.user import User
from utils.jwt_manager import generate_jwt

auth_router = APIRouter()

DB = SessionLocal()


@auth_router.post("/login", response_model=dict)
async def login(user: User) -> dict:
    if user.username == "platzi" and user.password == "platzi":
        return {"token": generate_jwt({"sub": user.username})}
    else:
        return {"message": "invalid credentials"}
