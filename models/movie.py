from sqlalchemy import Column, Integer, String, Float

from config.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    overview = Column(String, index=True)
    year = Column(Integer, index=True)
    rating = Column(Float, index=True)
    category = Column(String, index=True)
