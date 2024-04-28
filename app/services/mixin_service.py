from abc import ABC, abstractmethod

class ServiceMixin(ABC):

    @abstractmethod
    def get_db(self):
        ...
    
    @abstractmethod
    def get_table(self):
        ...
    
    @abstractmethod
    def get_query(self):
        ...

    @abstractmethod
    def get_by_id(self, id: int):
        ...

    @abstractmethod
    def create_instance(self, data: dict):
        ...

    @abstractmethod
    def delete_by_id(self,  id: int):
        ...

    @abstractmethod
    def get_instances(self):
        ...

    @abstractmethod
    def get_by_query(self, query):
        ...