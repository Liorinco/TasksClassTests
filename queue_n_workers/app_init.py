from flask import Flask
from celery import Celery


app = Flask("MyApp")
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery('tasks',
                broker=app.config['CELERY_BROKER_URL'],
                backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)


# @celery.task
# def test(self):
#     print "test"
