from tinydb import TinyDB, Query
from app.database.tinydb import TinyDBInstance


instance_db = TinyDBInstance()
name_table = 'table_test'
def test_database_class():
    assert type(instance_db.db) == TinyDB
    assert type(instance_db.query) == Query
    table = instance_db.get_or_create_table(name_table)
    assert table._name == name_table

def test_if_singleton_works():
    new_instance = TinyDBInstance()
    assert id(new_instance) == id(instance_db)