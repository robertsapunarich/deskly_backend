from pydantic import BaseModel

class TicketBase(BaseModel):
  title: str
  priority: str
  status: str

class TicketCreate(TicketBase):
  pass


class Ticket(TicketBase):
  id: int

  class Config:
    orm_mode = True

class TicketUpdate(TicketBase):
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