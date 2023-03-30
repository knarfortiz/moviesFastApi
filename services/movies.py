from models.movie import Movie
from schemas.movie import MovieTypeUpdate


class MovieService:

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        print(self.db)
        return self.db.query(Movie).all()

    def get_movie_by_id(self, movie_id: int):
        return self.db.query(Movie).filter(Movie.id == movie_id).first()

    def get_movie_by_category(self, category: str):
        return self.db.query(Movie).filter(Movie.category == category).all()

    def create_movie(self, movie: Movie):
        self.db.add(movie)
        self.db.commit()
        return movie

    def delete_movie(self, movie_id: int):
        movie = self.get_movie_by_id(movie_id)
        self.db.delete(movie)
        self.db.commit()
        return movie

    def update_movie(self, movie_id: int, old_movie: MovieTypeUpdate):
        movie = self.get_movie_by_id(movie_id)
        movie.title = old_movie.title
        movie.category = old_movie.category
        self.db.commit()
        return movie
