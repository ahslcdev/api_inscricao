
import json
import time
from fastapi.testclient import TestClient
import pytest
from app.apis.enrollment_api.tasks import add_enrollment_task
from app.apis.enrollment_api.exceptions import InvalidCPF
from app.apis.enrollment_api.main import app

from app.database.tinydb import TinyDBInstance
db = TinyDBInstance(name_db='db.json')

client = TestClient(app)

def test_add_enrollment_success(clear_db, celery_app):
    db.get_or_create_table('age_groups').insert({"min_age":10, "max_age":20})
    response = client.post(
        "enrollment/",
        content=json.dumps({"cpf":'61391989090', "age":10, "name":"teste"}),
    )

    assert response.status_code == 200

def test_add_enrollment_failure_cpf(clear_db, celery_app):
    response = client.post(
        "enrollment/",
        content=json.dumps({"cpf":'613919890902', "age":10, "name":"teste"}),
    )
    print(response.json())
    assert response.status_code == 400


def test_check_status_enrollment_success(clear_db, celery_app):
    db.get_or_create_table('age_groups').insert({"min_age":10, "max_age":20})
    response = client.post(
        "enrollment/",
        content=json.dumps({"cpf":'61391989090', "age":10, "name":"teste"}),
    )
    id = response.json().get('id')
    print(response.json())
    assert response.status_code == 200

    response = client.get(
        f"enrollment/check-status/{id}/"
    )
    assert response.status_code == 200
    assert response.json().get('message') == 'Inscrição pendente'
    add_enrollment_task.apply(queue='enrollment-queue')
    time.sleep(5)

    response = client.get(
        f"enrollment/check-status/{id}/"
    )
    assert response.status_code == 200
    assert response.json().get('message') == 'Inscrição aprovada'