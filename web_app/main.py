from fastapi import FastAPI
from fastapi.responses import JSONResponse

from celery import Celery
from celery.result import AsyncResult

app = FastAPI()

celery_app = Celery(
    'my_app',
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@app.get("/")
def root():
    return "hello world"

@app.post("/send_task")
async def send_task(x: int, y: int):
    # Send the task to the Celery worker
    task = celery_app.send_task('trigger_task', args = (x, y))
    return {'task_id': str(task.task_id), 'status': 'Processing'}

@app.get("/get_task/{task_id}")
async def get_task(task_id: str):
    # Send the task to the Celery worker
    task = AsyncResult(task_id)

    if task.ready():
        return {'task_id': str(task_id), 'status': str(task.status), 'result': str(task.result)}
    else:
        return {'task_id': str(task_id), 'status': str(task.status), 'result': str(task.result)}