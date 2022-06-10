# Stack:

    FastAPI: 
    Docker - RabbitMQ
    Celery

# Installation

## Create virtual environment

    python3 -m venv env

## Instance virtual environment

    source env/bin/activate

    # use "deactive" to desactive the virtual environment

## Install requirements

    pip3 install -r requirements.txt

## Install docker & docker images

    # Assuming that you are using ubuntu distros (>=20.04)
    sudo apt install docker.io
    
    # Installing the alpine version from rabbitmq
    docker run -it --rm --name rabbitmq -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq:3.10-alpine

    # Or you can use the normal version
    docker run -it --rm --name rabbitmq -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
    
    # Also the docker image will run afer the installation, see docker docs to expose a better handling of docker containers

    # https://docs.docker.com/engine/reference/commandline/cli/
    # https://hub.docker.com/_/rabbitmq


## Example of running the fastapi_celery experiment

    cd fastapi_celery

    # Start FastAPI project
    uvicorn app.app:app --reload

    # Open API Docs at: http://127.0.0.1:8000/docs

    # Initialize the celery workers
    celery -A worker.celery_worker.celery worker --loglevel=info

    # Observe the broker | queues manager
    celery flower -A worker.celery_worker.celery --broker:amqp://localhost//

    # Flower located at: http://localhost:5555

## Best Practices

If you need to install a new external python module, anchor the actual version that you are installing, example

    requirements.txt

    new-module==x.y.z

## References:

- [RabbitMQ - Hello Workd](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

- [Celery - Introduction to Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)

- [Medium - Azzan Amin - Celery Asynchronous Task Queues with Flower & FastAPI](https://medium.com/thelorry-product-tech-data/celery-asynchronous-task-queue-with-fastapi-flower-monitoring-tool-e7135bd0479f)

## TODO
- Expose a recipe about how to use the "pika" experiment.