from celery import Celery


app = Celery('proj')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
