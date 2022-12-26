from celery import Celery
import time

celery_app = Celery(
    'my_app',
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@celery_app.task(name="trigger_task")
def trigger_task(x, y):
    # Perform the task here
    print("in trigger_task", x, y)
    time.sleep(5)
    
    return y