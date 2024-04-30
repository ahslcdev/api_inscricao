from fastapi import APIRouter, FastAPI, Request
from app.apis.age_api.service import AgeGroupService
from app.tests.fixtures import *
import json
from fastapi.testclient import TestClient
from app.apis.age_api.main import app

from app.database.tinydb import TinyDBInstance
from app.tests.utils import replace_to_exception  
db = TinyDBInstance(name_db='db.json')

client = TestClient(app)

def test_http_methods_without_auth():
    """
    Teste verifica se é possível acessar algum endpoint sem AUTH.
    """
    response_post = client.post(
        "group-age/",
        content=json.dumps({"min_age":1900, "max_age":2000})
    )

    assert response_post.status_code == 401
    response_get = client.get(
        "group-age/"
    )

    assert response_get.status_code == 401

    response_get_id = client.get(
        "group-age/123/"
    )
    assert response_get_id.status_code == 401

    responst_delete = client.delete(
        "group-age/123/"
    )
    assert responst_delete.status_code == 401


def test_add_age_group_success(clear_db, basic_auth_credentials):
    """
    Teste verifica se é possível cadastrar um novo grupo de idades.
    """
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1900, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 200
    assert response.json() == {"min_age":1900, "max_age":2000}
    

def test_add_age_group_failure(clear_db, basic_auth_credentials):
    """
    Teste verifica que não é possível cadastrar o mesmo grupo de idades.
    É verificado também se é possível cadastrar um grupo de idades com
    a idade minima sendo maior que a máxima.
    """
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1900, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 200
    assert response.json() == {"min_age":1900, "max_age":2000}
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1900, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 400

    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":300, "max_age":200}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 400


def test_list_age_group_success(clear_db, basic_auth_credentials):
    response = client.get(
        "group-age/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 200
    assert type(response.json()) == list


def test_retrieve_age_group_success(clear_db, basic_auth_credentials):
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1500, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )

    response = client.get(
        f"group-age/3/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 200
    assert type(response.json()) == dict


def test_retrieve_age_group_failure(monkeypatch: pytest.MonkeyPatch,
                                    clear_db, basic_auth_credentials):
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1600, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    
    response = client.get(
        f"group-age/15000/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 404
    assert type(response.json()) == dict

    monkeypatch.setattr("app.apis.age_api.service.AgeGroupService.get_by_id", replace_to_exception)
    last_item = db.get_or_create_table('age_groups').all()[-1]
    response = client.get(
        f"group-age/{last_item.doc_id}/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 400
    assert type(response.json()) == dict


def test_list_age_group_failure(monkeypatch: pytest.MonkeyPatch, basic_auth_credentials):
    monkeypatch.setattr("app.apis.age_api.service.AgeGroupService.get_instances", replace_to_exception)
    
    response = client.get(
        "group-age/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Algo inesperado aconteceu, entre em contato com o suporte."}


def test_delete_age_group_success(clear_db, basic_auth_credentials):
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1500, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    last_item = db.get_or_create_table('age_groups').all()[-1]
    response = client.delete(
        f"group-age/{last_item.doc_id}/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 200
    assert type(response.json()) == dict


def test_delete_age_group_failure(monkeypatch: pytest.MonkeyPatch,
                                    clear_db, basic_auth_credentials):
    response = client.post(
        "group-age/",
        content=json.dumps({"min_age":1600, "max_age":2000}),
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    
    response = client.delete(
        f"group-age/15000/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 404
    assert type(response.json()) == dict

    monkeypatch.setattr("app.apis.age_api.service.AgeGroupService.delete_by_id", replace_to_exception)
    last_item = db.get_or_create_table('age_groups').all()[-1]
    response = client.delete(
        f"group-age/{last_item.doc_id}/",
        headers={"Authorization": f"Basic {basic_auth_credentials}"}
    )
    assert response.status_code == 400
    assert type(response.json()) == dict