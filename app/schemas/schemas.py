from pydantic import BaseModel

class TaskBase(BaseModel):
  title: str
  priority: str
  status: str

class TaskCreate(TaskBase):
  pass


class Task(TaskBase):
  id: int

  class Config:
    orm_mode = True

class TaskUpdate(TaskBase):
  pass

class UserBase(BaseModel):
  email: str
  type: str

class UserCreate(UserBase):
  password: str


class User(UserBase):
  id: int

  class Config:
    orm_mode = True