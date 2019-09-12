import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'borrowDomain.settings')

app = Celery('borrowDomain', backend='amqp',
broker='amqp://<userdjango>:<userdjango>@<127.0.0.1>/<userdjangohost>')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 