from sqlalchemy.orm import Session
from app.schemas import schemas
from app.db import models

def get_ticket(db: Session, ticket_id: int) -> models.Ticket:
  return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def get_tickets(db: Session, skip: int = 0, limit: int = 100) -> list[models.Ticket]:
  return db.query(models.Ticket).offset(skip).limit(limit).all()

def create_ticket(db: Session, ticket: schemas.TicketCreate) -> models.Ticket:
  db_ticket = models.Ticket(**ticket.model_dump())
  db.add(db_ticket)
  db.commit()
  db.refresh(db_ticket)
  return db_ticket

def update_ticket(db: Session, ticket_id: int, ticket: schemas.TicketUpdate) -> models.Ticket:
  db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
  db_ticket.title = ticket.title
  db_ticket.priority = ticket.priority
  db_ticket.status = ticket.status
  db.commit()
  db.refresh(db_ticket)
  return db_ticket