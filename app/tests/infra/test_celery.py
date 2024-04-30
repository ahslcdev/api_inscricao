import os
from app.celery import celery

def test_celery_file():
    assert os.environ.get('CELERY_BROKER_URL') == celery.celery._conf.broker_url
    assert os.environ.get('CELERY_RESULT_BACKEND') == celery.celery._conf.result_backend