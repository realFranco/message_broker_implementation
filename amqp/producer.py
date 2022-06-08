import amqp

with amqp.Connection('localhost') as c:
    ch = c.channel()
    ch.basic_publish(amqp.Message('Hello World'), routing_key='order_notify')
