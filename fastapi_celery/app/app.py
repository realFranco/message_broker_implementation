"""
uvicorn app.app:app --reload

http://127.0.0.1:8000/docs#/default/add_order_order_post

celery flower -A worker.celery_worker.celery --broker:amqp://localhost//

celery flower -A celery_worker.celery -Q celery,payment --broker:amqp://localhost//

celery flower -A worker.celery_worker.celery worker -Q celery,payment --broker:amqp://localhost//

http://localhost:5555
"""
import traceback

from fastapi import FastAPI

from model.order import Order
from worker.celery_worker import create_order, create_order_async

# Create FastAPI app
app = FastAPI()

# Create order endpoint
@app.post('/order')
def add_order(order: Order):
    try:
        # use delay() method to call the celery task
        create_order.delay(order.customer_name, order.order_quantity)
        # create_order.apply_async((order.customer_name, order.order_quantity),
        #     exchange='payment', routing_key='actor.lopri')
        return {"message": "Order Received! Thank you for your patience."}

    except Exception as err:
        traceback.print_exc()
        print(f'[ERR] at add order: {str(err)}')
        return {"message": "Order not received! we will investigate the error"}


# Create order endpoint
@app.post('/order/async')
async def add_order_async(order: Order):
    # use delay() method to call the celery task
    create_order_async.delay(order.customer_name, order.order_quantity)
    # create_order_async.apply_async((order.customer_name, order.order_quantity),
    #     exchange='payment', routing_key='actor.hipri')
    return {"message": "Async Order Received! Thank you for your patience."}
