from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from schemas import schemas
from crud import crud
from db.database import SessionLocal, engine
from db import models

# class Ticket(BaseModel):
#   title: str
#   priority: str
#   status: str
  
# fake_db = {
#   1: Ticket(title="Fix all the bugs", priority="high", status="open"),
#   2: Ticket(title="Write some docs", priority="medium", status="open"), 
#   3: Ticket(title="Release the product", priority="high", status="closed"),
# }

app = FastAPI()

# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/")
async def read_main():
  return {"message": "Hello, World!"}


@app.get("/tasks", response_model=list[schemas.Task])
async def read_tasks(status: str | None = None, db: Session = Depends(get_db)) -> list[schemas.Task]:
  if status:
    db_tasks = crud.get_tasks_by_status(db, status)
  else:
    db_tasks = crud.get_tasks(db)
  return list(db_tasks)


@app.put("/task/{task_id}", response_model=schemas.Task)
async def update_task(task_id: int, task_params: schemas.TaskUpdate) -> schemas.Task:
    task = crud.update_task(task_id, task_params)
    return task

