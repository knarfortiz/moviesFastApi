from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException

from utils.jwt_manager import validate_jwt


class JwtBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_jwt(auth.credentials)
        if data["sub"] != "platzi":
            raise HTTPException(status_code=401, detail="Invalid email")
