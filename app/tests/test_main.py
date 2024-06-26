from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine

# Create a test database
engine = create_engine("sqlite:///./test.db")
with engine.connect() as connection:
  connection.execute("CREATE TABLE tickets (id INTEGER PRIMARY KEY, title TEXT, priority TEXT, status TEXT)")
  connection.execute("INSERT INTO tickets (title, priority, status) VALUES ('Fix all the bugs', 'high', 'open')")
  connection.execute("INSERT INTO tickets (title, priority, status) VALUES ('Write some docs', 'medium', 'open')")
  connection.execute("INSERT INTO tickets (title, priority, status) VALUES ('Release the product', 'high', 'closed')")

# Create a test client
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
  response = client.put("/ticket/1", json={"title": "Fix all the bugs", "priority": "high", "status": "closed"})
  assert response.status_code == 200
  assert response.json() == {"title": "Fix all the bugs", "priority": "high", "status": "closed"}

def test_update_ticket_not_found():
  response = client.put("/ticket/4", json={"title": "Fix all the bugs", "priority": "high", "status": "open"})
  assert response.status_code == 404
  assert response.json() == {"detail": "Ticket not found"}