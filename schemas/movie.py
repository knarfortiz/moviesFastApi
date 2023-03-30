from typing import Optional

from pydantic import BaseModel, Field


class MovieTypeCreate(BaseModel):
    id: int | None = None
    title: str = Field(max_length=100)
    overview: str
    year: int
    rating: float = Field(ge=0, le=10)
    category: str = Field(max_length=10, min_length=3)

    class Config:
        schema_extra = {
            "example": {
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }


class MovieTypeUpdate(BaseModel):
    title: Optional[str]
    overview: Optional[str]
    year: Optional[int]
    rating: Optional[float]
    category: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }
