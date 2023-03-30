from fastapi import FastAPI

from middleware.error_handler import ErrorHandler
from routers.auth import auth_router
from routers.movie import movie_router
from config.database import SessionLocal, engine, Base

DB = SessionLocal()

app = FastAPI()
app.title = "FastAPI course beginner Platzi"
app.version = "0.1.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router, prefix="/api/movies", tags=["Movies"])
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World!!!"}


@app.get("/hello/{name}", tags=["Hola"])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
