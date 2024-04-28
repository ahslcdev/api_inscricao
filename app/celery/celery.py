import os
from celery import Celery
from app.configs.settings import Settings

settings = Settings()
# celery = Celery(
#     __name__,
#     broker='amqp://rabbit_user:rabbit_password@broker-rabbitmq:5672/',#os.environ.get('CELERY_BROKER_URL'),
#     backend='redis://redis:6379/0'#os.environ.get('CELERY_RESULT_BACKEND')
# )
print(os.environ.get('CELERY_BROKER_URL'))

celery = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery.autodiscover_tasks(['app.celery.enrollment_tasks'])