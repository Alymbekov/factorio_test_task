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


@app.post("/run-task/")
def start_task():
    import json
    from scraping.worker import WorkerBroker
    url = "https://factorioprints.com/top"
    task = {'url': url}
    task = json.dumps(task)
    wb = WorkerBroker('worker-queue', 10)
    message = json.dumps(task)
    wb.produce_message(message=message, priority=1)
    return {"msg": "Successfully started task"}
