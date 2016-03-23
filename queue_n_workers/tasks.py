from celery import Celery
# from celery import current_app
# from celery.contrib.methods import task


app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


class Tasks(object):
    """docstring for Tasks"""
    def __init__(self):
        super(Tasks, self).__init__()
        self.tasks = {
            "test": self.test
        }

        # app = Celery('tasks',
        #              broker='redis://localhost:6379/0',
        #              backend='redis://localhost:6379/0')

    @app.task()
    def test(self):
        print "test"
