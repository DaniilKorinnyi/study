import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_schedule': {
        'task': 'user.tasks.print_datetime',
        'schedule': 5,
        'args': (),
        'kwargs': {},
    }
}