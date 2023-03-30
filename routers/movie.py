from fastapi import APIRouter, Path, Query, status, Depends

from config.database import SessionLocal
from middleware.jwt_bearer import JwtBearer
from traits.custom_response import assert_response, error_response
from utils.Constants import movies
from models.movie import Movie as MovieModel
from schemas.movie import MovieTypeCreate, MovieTypeUpdate
from services.movies import MovieService

movie_router = APIRouter()

DB = SessionLocal()


@movie_router.get("/",
                  response_model=list[MovieTypeCreate],
                  status_code=status.HTTP_200_OK,
                  dependencies=[Depends(JwtBearer())]
                  )
async def get_movies() -> list[MovieTypeCreate]:
    print(DB)
    result = MovieService(DB).get_movies()
    return assert_response(status.HTTP_200_OK, result)


@movie_router.get("/by-category")
async def get_movies_by_category(category: str = Query(min_length=3, max_length=10)):
    print(category)
    result = MovieService(DB).get_movie_by_category(category)
    if not result:
        return error_response(status.HTTP_404_NOT_FOUND, {"message": "Movie not found"})
    return assert_response(status.HTTP_200_OK, result)


@movie_router.get("/{movie_id}", response_model=MovieTypeUpdate)
async def get_movie(movie_id: int = Path(ge=1, le=10)):
    result = MovieService(DB).get_movie_by_id(movie_id)
    if not result:
        return error_response(status.HTTP_404_NOT_FOUND, {"message": "Movie not found"})
    return assert_response(status.HTTP_200_OK, result)


@movie_router.post("/", response_model=MovieTypeCreate, status_code=status.HTTP_201_CREATED)
async def create_movie(movie: MovieTypeCreate) -> dict:
    try:
        new_movie = MovieModel(**movie.dict())
        MovieService(DB).create_movie(new_movie)
        return assert_response(status.HTTP_201_CREATED, {"message": "Movie created successfully"})
    except Exception as e:
        return error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": f"Error: {e}"})


@movie_router.delete("/{movie_id}")
async def delete_movie(movie_id: int):
    MovieService(DB).delete_movie(movie_id)
    return {"message": "movie deleted", "movies": movies}


@movie_router.put("/{movie_id}")
async def update_movie(movie_id: int, movie: MovieTypeUpdate) -> dict:
    MovieService(DB).update_movie(movie_id, movie)
    return {"message": "movie updated", "movies": movies}
