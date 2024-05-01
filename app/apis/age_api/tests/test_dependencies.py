import base64
from fastapi.testclient import TestClient
from app.apis.age_api.main import app

client = TestClient(app)

def test_check_credentials():
    """"
    Este teste é utilizado para testar o EXCEPTION da dependencia check_credentials,
    os casos de sucesso não foram inseridos pois já são devidamente testados
    nas chamadas HTTP realizadas nos testes de routes.
    """
    usuario = "admin"
    senha = "wrong_password"
    usuario_senha = f"{usuario}:{senha}"
    credenciais_base64 = base64.b64encode(usuario_senha.encode()).decode()

    response = client.get(
        "group-age/",
        headers={"Authorization": f"Basic {credenciais_base64}"}
    )
    assert response.status_code == 401
    assert type(response.json()) == dict

    