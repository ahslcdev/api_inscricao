import pytest
from app.enrollment_api.exceptions import InvalidAge
from app.tests.fixtures import clear_db
from app.enrollment_api.schemas import EnrollmentSchema
from app.database.tinydb import TinyDBInstance

from app.enrollment_api.utils import validate_age, validate_cpf

db = TinyDBInstance(name_db='db.json')

def test_validate_cpf():
    cpf_success = '61391989090'
    cpf_len_error = '123'
    cpf_error = '12345678912'
    cpf_equals_digits = '11111111111'

    assert validate_cpf(cpf_success) == True
    assert validate_cpf(cpf_len_error) == False
    assert validate_cpf(cpf_error) == False
    assert validate_cpf(cpf_equals_digits) == False


def test_valid_age_less_than_zero(clear_db):
    with pytest.raises(InvalidAge) as e: 
        validate_age(0)
    assert str(e.value) == 'Idade não pode ser menor que 0'


def test_valid_age_not_in_db(clear_db):
    with pytest.raises(InvalidAge) as e: 
        validate_age(150)
    assert str(e.value) == 'Esta idade não está disponível.'