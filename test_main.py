from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello, World!"}

def test_read_tickets():
  response = client.get("/tickets")
  assert response.status_code == 200
  assert len(response.json()) == 3
  assert response.json() == [
    {"title": "Fix all the bugs", "priority": "high", "status": "open"},
    {"title": "Write some docs", "priority": "medium", "status": "open"},
    {"title": "Release the product", "priority": "high", "status": "closed"},
  ]

def test_read_tickets_with_status():
  response = client.get("/tickets?status=open")
  assert response.status_code == 200
  assert len(response.json()) == 2
  assert response.json() == [
    {"title": "Fix all the bugs", "priority": "high", "status": "open"},
    {"title": "Write some docs", "priority": "medium", "status": "open"},
  ]

def test_update_ticket():
  response = client.put("/tickets/1", json={"title": "Fix all the bugs", "priority": "high", "status": "closed"})
  assert response.status_code == 200
  assert response.json() == {"ticket_id": 1, "ticket": {"title": "Fix all the bugs", "priority": "high", "status": "closed"}}

def test_update_ticket_not_found():
  response = client.put("/tickets/4", json={"title": "Fix all the bugs", "priority": "high", "status": "open"})
  assert response.status_code == 404
  assert response.json() == {"detail": "Ticket not found"}