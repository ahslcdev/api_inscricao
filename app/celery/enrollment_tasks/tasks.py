import time
from app.celery.celery import celery
from app.enrollment_api.service import EnrollmentService

@celery.task
def add_enrollment_task(data: dict):
    time.sleep(20)
    id = EnrollmentService().create_instance(data)
    return id