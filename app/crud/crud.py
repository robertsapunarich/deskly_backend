from sqlalchemy.orm import Session
from schemas import schemas
from db.models import Task

def get_task(db: Session, task_id: int) -> Task:
  return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> list[Task]:
  return db.query(Task).offset(skip).limit(limit).all()

def get_tasks_by_status(db: Session, status: str) -> list[Task]:
  return db.query(Task).filter(Task.status == status).all()

def create_task(db: Session, task: schemas.TaskCreate) -> Task:
  task = Task(**Task.model_dump())
  db.add(task)
  db.commit()
  db.refresh(task)
  return task

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate) -> Task:
  db_task = db.query(Task).filter(Task.id == task_id).first()
  db_task.title = task.title
  db_task.priority = task.priority
  db_task.status = task.status
  db.commit()
  db.refresh(db_task)
  return db_task