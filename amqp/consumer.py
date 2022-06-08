import amqp

with amqp.Connection('localhost') as c:
    ch = c.channel()
    def on_message(message):
        print('Received message (delivery tag: {}): {}'.format(message.delivery_tag, message.body))
        ch.basic_ack(message.delivery_tag)
    ch.basic_consume(queue='order_notify', callback=on_message)
    while True:
        c.drain_events()
