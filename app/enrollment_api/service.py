from app.database.tinydb import TinyDBInstance
from celery.result import AsyncResult

from app.services.mixin_service import ServiceMixin

class EnrollmentService(ServiceMixin):

    def get_db(self):
        return TinyDBInstance()
    
    def get_table(self):
        return self.get_db().get_or_create_table('enrollments')
    
    def get_query(self):
        return self.get_db().query
    
    def create_instance(self, enrollment: dict):
        table = self.get_table()
        enrollment_id = table.insert(enrollment)
        return enrollment_id
    
    def get_status_enrollment(self, id: str):
        status: bool = AsyncResult(id)
        return status.ready()