from tinydb import TinyDB, Query
from app.configs.settings import Settings

from app.singleton import SingletonMeta

class TinyDBInstance(metaclass=SingletonMeta):
    def __init__(self, name_db: str = Settings().DATABASE_PATH) -> None:
        self.__db = TinyDB(name_db)

    @property
    def db(self) -> TinyDB:
        return self.__db
    
    @property
    def query(self):
        return Query()
    
    def get_or_create_table(self, table_name):
        return self.db.table(table_name)