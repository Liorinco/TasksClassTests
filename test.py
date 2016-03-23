from queue_n_workers.tasks import Tasks
# from queue_n_workers.worker_init import app


tasks = Tasks()
tasks.test.delay()
