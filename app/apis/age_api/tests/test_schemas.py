# from app.tests.fixtures import clear_db
from app.apis.age_api.schemas import AgeGroup
from app.database.tinydb import TinyDBInstance

db = TinyDBInstance(name_db='db.json')

def test_to_dict(clear_db):
    """
    Este teste serve apenas para testar o método to_dict
    """
    age_group = AgeGroup(min_age=5, max_age=10)
    assert age_group.to_dict() == {"min_age": 5, "max_age": 10}