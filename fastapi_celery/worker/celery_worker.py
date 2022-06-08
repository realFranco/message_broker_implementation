"""
celery -A worker.celery_worker.celery worker --loglevel=info

types of workers:
https://www.vultr.com/docs/asynchronous-task-queueing-in-python-using-celery/#:~:text=Celery%20is%20a%20task%20queue,your%20tasks%20synchronously%20or%20asynchronously.

"""

from time import sleep
import asyncio

from celery import Celery
from celery.utils.log import get_task_logger

# Initialize celery
celery = Celery('tasks', broker='amqp://guest:guest@127.0.0.1:5672//')

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

# Create Order - Run Asynchronously with celery
# Example process of long running task
@celery.task
def create_order(name, quantity):
    
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

@celery.task
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
