import os
from celery import Celery
from app.configs.settings import Settings

settings = Settings()

celery = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery.autodiscover_tasks(['app.apis.enrollment_api.tasks'])