from celery import Celery

# See this link for basic setup of Celery w/ RabbitMQ -> http://bit.ly/2lVefZx
app = Celery('celery_app', broker='amqp://guest@localhost//', backend='amqp://')
