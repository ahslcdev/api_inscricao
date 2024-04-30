from pytest_mock import mocker
from abc import ABC, ABCMeta
from app.services.mixin_service import ServiceMixin


def test_service_mixin(mocker):
    ServiceMixin.__abstractmethods__ = set()

    # @dataclass
    class Dummy(ServiceMixin):
        pass

    instance = Dummy()
    db = instance.get_db()
    table = instance.get_table()
    query = instance.get_query()
    by_id = instance.get_by_id(5)
    create_instance = instance.create_instance({})
    delete = instance.delete_by_id(5)
    instances = instance.get_instances()
    by_query = instance.get_by_query({})

    assert db is None
    assert table is None
    assert query is None
    assert by_id is None
    assert create_instance is None
    assert delete is None
    assert instances is None
    assert by_query is None