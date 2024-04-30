import base64
import json
import pytest

@pytest.fixture()
def clear_db():
    yield
    with open('db.json', 'w') as f:
        json.dump({}, f)
    

@pytest.fixture
def basic_auth_credentials():
    usuario = "admin"
    senha = "Password123"
    usuario_senha = f"{usuario}:{senha}"
    credenciais_base64 = base64.b64encode(usuario_senha.encode()).decode()
    return credenciais_base64