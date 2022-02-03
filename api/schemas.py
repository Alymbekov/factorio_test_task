from typing import Optional
from pydantic import BaseModel


class Author(BaseModel):
    id: int
    author: str
    favorites: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True


class Information(BaseModel):
    id: int
    author_id: int
    body: str
    blue_print_string: str
    image: str

    class Config:
        orm_mode = True
