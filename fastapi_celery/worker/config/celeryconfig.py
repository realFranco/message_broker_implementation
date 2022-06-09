# ref: https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html?highlight=Oslo#configuration


class Config:
    # broker_url = 'pyamqp://'
    # broker_url = 'amqp://guest:guest@127.0.0.1:5672//'
    result_backend = 'rpc://'

    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timeozne = 'Chile/Continental'
    enable_utc = True

    task_queues = {
        'celery': {
            'exchange': 'celery',
            # 'routing_key': 'cpubound',
        },
        'payment': {
            'exchange': 'celery',
            # 'routing_key': 'cpubound',
        }
    }

    # Defining the exchanges & queue where the tasks are interested in consume
    task_routes = {
        'create_order': {
            'queue': 'celery',
            'exchange': 'celery',
            # 'routing_key': 'actor.lopri',
        },
        'create_order_async': {
            'queue': 'payment',
            'exchange': 'celery',
            # 'routing_key': 'actor.hipri',
        }
    }
