from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

class Ticket(BaseModel):
  title: str
  priority: str
  status: str
  
fake_db = {
  1: Ticket(title="Fix all the bugs", priority="high", status="open"),
  2: Ticket(title="Write some docs", priority="medium", status="open"), 
  3: Ticket(title="Release the product", priority="high", status="closed"),
}

app = FastAPI()

@app.get("/")
async def read_main():
  return {"message": "Hello, World!"}


@app.get("/tickets")
async def read_tickets(status: str | None = None) -> list[Ticket]:
  if status:
    return [ticket for ticket in fake_db.values() if ticket.status == status]
  return list(fake_db.values())


@app.put("/ticket/{ticket_id}")
async def update_ticket(ticket_id: int, ticket_params: Ticket) -> Ticket:
  try:
    if fake_db[ticket_id]:
      fake_db[ticket_id] = ticket_params
      return fake_db[ticket_id]
  except KeyError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

