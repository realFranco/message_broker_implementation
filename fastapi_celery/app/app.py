"""
uvicorn app.app:app --reload

http://127.0.0.1:8000/docs#/default/add_order_order_post

celery flower -A celery_worker.celery --broker:amqp://localhost//

http://localhost:5555
"""
from fastapi import FastAPI
from model.order import Order
from worker.celery_worker import create_order, create_order_async

# Create FastAPI app
app = FastAPI()

# Create order endpoint
@app.post('/order')
def add_order(order: Order):
    # use delay() method to call the celery task
    create_order.delay(order.customer_name, order.order_quantity)
    return {"message": "Order Received! Thank you for your patience."}


# Create order endpoint
@app.post('/order/async')
async def add_order(order: Order):
    # use delay() method to call the celery task
    create_order_async.delay(order.customer_name, order.order_quantity)
    return {"message": "Async Order Received! Thank you for your patience."}
