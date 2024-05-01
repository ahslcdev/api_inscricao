from app.database.tinydb import TinyDBInstance
from celery.result import AsyncResult

from app.apis.enrollment_api.schemas import EnrollmentSchema
from app.services.mixin_service import ServiceMixin

class EnrollmentService(ServiceMixin):

    def get_db(self):
        return TinyDBInstance()
    
    def get_table(self):
        return self.get_db().get_or_create_table('enrollments')
    
    def get_query(self):
        return self.get_db().query
    
    def create_instance(self, enrollment: EnrollmentSchema):
        table = self.get_table()
        enrollment_id = table.insert(enrollment)
        return enrollment_id
    
    def get_status_enrollment(self, id: str):
        status: bool = AsyncResult(id)
        return status.ready()
    
    def delete_by_id(self, id: int):
        ...
    
    def get_by_query(self, query):
        ...

    def get_instances(self):
        ...

    def get_by_id(self, id: int):
        ...