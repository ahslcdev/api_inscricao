
from fastapi.testclient import TestClient
from app.enrollment_api.main import app
client = TestClient(app)