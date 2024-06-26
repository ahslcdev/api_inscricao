import time
from app.celery.celery import celery
from app.apis.enrollment_api.service import EnrollmentService

@celery.task
def add_enrollment_task(data: dict):
    """
    Task responsável por adicionar uma nova inscrição ao banco de dados
    """
    time.sleep(2)
    id = EnrollmentService().create_instance(data)
    return id