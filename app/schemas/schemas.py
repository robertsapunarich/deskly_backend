from pydantic import BaseModel

class CustomerBase(BaseModel):
    email: str

class CustomerCreate(CustomerBase):
    password: str

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class AssigneeBase(BaseModel):
    email: str

class AssigneeCreate(AssigneeBase):
    password: str

class Assignee(AssigneeBase):
    id: int

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    body: str
    subject: str
    thread_id: int

class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True

class ThreadBase(BaseModel):
    title: str

class ThreadCreate(ThreadBase):
    pass

class Thread(ThreadBase):
    id: int
    messages: list[Message] = []
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    priority: str
    status: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    assignee: Assignee
    pass

class Task(TaskBase):
    id: int
    thread: Thread
    assignee: Assignee
    customer: Customer

    class Config:
        orm_mode = True
