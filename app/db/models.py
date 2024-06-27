from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    type = Column(String)

    __mapper_args__ = {
      "polymorphic_identity": "users",
      "polymorphic_on": type,
    }

class Assignee(User):
    __mapper_args__ = {
      "polymorphic_identity": "assignees",
    }

    tasks = relationship("Task", back_populates="assignee", foreign_keys="Task.assignee_id")

class Customer(User):
    __mapper_args__ = {
      "polymorphic_identity": "customers",
    }

    tasks = relationship("Task", back_populates="customer", foreign_keys="Task.customer_id")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    priority = Column(String)
    status = Column(String, default="open")
    assignee_id = Column(Integer, ForeignKey("users.id"))
    customer_id = Column(Integer, ForeignKey("users.id"))

    assignee = relationship("Assignee", back_populates="tasks", foreign_keys=[assignee_id])
    customer = relationship("Customer", back_populates="tasks", foreign_keys=[customer_id])

    thread = relationship("Thread", back_populates="task", uselist=False)

class Thread(Base):
    __tablename__ = "threads"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    task_id = Column(Integer, ForeignKey("tasks.id"))

    task = relationship("Task", back_populates="thread")
    messages = relationship("Message", back_populates="thread")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    body = Column(String)
    thread_id = Column(Integer, ForeignKey("threads.id"))

    thread = relationship("Thread", back_populates="messages")
