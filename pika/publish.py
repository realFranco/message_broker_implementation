import json

import pika



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

notify = {
    'mesage': 'Hello notify'
}
channel.basic_publish(
    exchange='order', 
    routing_key='order.notify',
    body=json.dumps(notify)
)

print(' [x] Sent notify message')

report = {
    'mesage': 'Hello report'
}
channel.basic_publish(
    exchange='order', 
    routing_key='order.report',
    body=json.dumps(report)
)
print(' [x] Sent report message')
connection.close()