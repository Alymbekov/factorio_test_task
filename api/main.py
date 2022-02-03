from typing import List

from fastapi import FastAPI

from api import schemas
from database import operations

app = FastAPI()


@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 100):
    authors = operations.get_authors(skip=skip, limit=limit)
    return authors


@app.get("/information/", response_model=List[schemas.Information])
def read_information(skip: int = 0, limit: int = 100):
    information = operations.get_information(skip=skip, limit=limit)
    return information


