from app.apis.age_api.schemas import AgeGroup
from app.database.tinydb import TinyDBInstance
from app.services.mixin_service import ServiceMixin


class AgeGroupService(ServiceMixin):

    def get_db(self):
        """
        Retorna a instancia do banco de dados
        """
        return TinyDBInstance()
    
    def get_table(self):
        """
        Retorna a tabela que se irá realizar as operações de CRUD
        """
        return self.get_db().get_or_create_table('age_groups')
    
    def get_query(self):
        """
        Retorna uma instancia da classe QUERY.
        """
        return self.get_db().query
    
    def get_by_id(self, id: int):
        """
        Retorna o objeto com o ID informado
        """
        table = self.get_table()
        age = table.get(doc_id=id)
        return age

    def create_instance(self, age: AgeGroup):
        """
        Cria um registro no banco de dados com os dados informados
        """
        table = self.get_table()
        age_dict = age.model_dump()
        age_id = table.insert(age_dict)
        return self.get_by_id(age_id)

    def delete_by_id(self,  id: int):
        """
        Deleta um registro do banco de dados com base no ID informado
        """
        table = self.get_table()
        table.remove(doc_ids=[id])

    def get_instances(self):
        """
        Retorna todos os registros da tabela
        """
        table = self.get_table()
        ages: list = table.all()
        return ages
    
    def get_by_query(self, values):
        """
        Retorna uma lista de registros com base na query informada
        """
        table = self.get_table()
        ages: list = table.search(values)
        return ages