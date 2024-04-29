from app.age_api.schemas import AgeGroup
from app.database.tinydb import TinyDBInstance
from app.services.mixin_service import ServiceMixin


class AgeGroupService(ServiceMixin):

    def get_db(self):
        return TinyDBInstance()
    
    def get_table(self):
        return self.get_db().get_or_create_table('age_groups')
    
    def get_query(self):
        return self.get_db().query
    
    def get_by_id(self, id: int):
        table = self.get_table()
        age: dict = table.get(doc_id=id)
        return age

    def create_instance(self, age: AgeGroup):
        table = self.get_table()
        age_dict = age.dict()
        age_id = table.insert(age_dict)
        return self.get_by_id(age_id)

    def delete_by_id(self,  id: int):
        table = self.get_table()
        table.remove(doc_id=id)

    def get_instances(self):
        table = self.get_table()
        ages: list = table.all()
        return ages
    
    def get_by_query(self, values):
        table = self.get_table()
        ages: list = table.search(values)
        return ages