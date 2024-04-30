from app.database.tinydb import TinyDBInstance
from celery.result import AsyncResult

from app.enrollment_api.schemas import EnrollmentSchema
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
        # return super().delete_by_id(id)
    
    def get_by_query(self, query):
        ...
        # return super().get_by_query(query)

    def get_instances(self):
        ...
        # return super().get_instances()

    def get_by_id(self, id: int):
        ...
        # return super().get_by_id(id)