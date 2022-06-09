"""
celery -A worker.celery_worker.celery worker --loglevel=info

# If many queues are requiered
celery -A worker.celery_worker.celery worker -Q celery,payment --loglevel=info

types of workers:
https://www.vultr.com/docs/asynchronous-task-queueing-in-python-using-celery/#:~:text=Celery%20is%20a%20task%20queue,your%20tasks%20synchronously%20or%20asynchronously.

"""

from time import sleep
import asyncio
import traceback

from celery import Celery
from celery.utils.log import get_task_logger

from worker.config.celeryconfig import Config


# Initialize celery
celery = Celery('tasks')

# Config applied into celery instance
# celery.config_from_object('worker.config.celeryconfig:Config')
celery.config_from_object(Config)

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

# Create Order - Run Asynchronously with celery
# Example process of long running task
def fail_function():
    return None

@celery.task(name='create_order', acks_late=True)
def create_order(name, quantity):
    # Inducing an error, comment the next line and the function will be completed
    # fake_list = [] + fail_function()

    # 5 seconds per 1 order
    complete_time_per_item = 5

    # Keep increasing depending on item quantity being ordered
    sleep(complete_time_per_item * quantity)

    # Display log
    celery_log.info(f"Order Complete!")
    return {"message": f"Hi {name}, Your order has completed!",
            "order_quantity": quantity}

async def some_function(name: str) -> None:
    print(f'{name}: Your async function was executed!')
    return

@celery.task(name='create_order_async', acks_late=True)
def create_order_async(name, quantity):
    
    # 5 seconds per 1 order
    complete_time_per_item = 5
    
    # Keep increasing depending on item quantity being ordered
    sleep(complete_time_per_item * quantity)

    asyncio.run(some_function(name=name))

    # Display log    
    celery_log.info(f"Async Order Complete!")

    return {"message": f"Hi {name}, Your async order has completed!",
            "order_quantity": quantity}
