import base64
from fastapi.testclient import TestClient
from app.age_api.main import app

client = TestClient(app)

def test_check_credentials():
    usuario = "admin"
    senha = "wrong_password"
    usuario_senha = f"{usuario}:{senha}"
    credenciais_base64 = base64.b64encode(usuario_senha.encode()).decode()
    # return credenciais_base64

    response = client.get(
        "group-age/",
        headers={"Authorization": f"Basic {credenciais_base64}"}
    )
    
    # response = client.delete(
    #     f"group-age/15000/",
    #     headers={"Authorization": f"Basic {basic_auth_credentials}"}
    # )
    # assert response.status_code == 404
    # assert type(response.json()) == dict

    # monkeypatch.setattr("app.age_api.service.AgeGroupService.delete_by_id", replace_to_exception)
    # last_item = db.get_or_create_table('age_groups').all()[-1]
    # response = client.delete(
    #     f"group-age/{last_item.doc_id}/",
    #     headers={"Authorization": f"Basic {basic_auth_credentials}"}
    # )
    print(response.json())
    assert response.status_code == 401
    assert type(response.json()) == dict

    