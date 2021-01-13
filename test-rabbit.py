#!/usr/bin/env python
# import sys, os

# import pika, sys, os
# from rabbitmq import RabbitMQ
import rabbitmq

# Init object
rabbit = rabbitmq.RabbitMQ()

# RabbitMQ connection
rabbit.connection_rabbitmq()

# Declraring queues
rabbit.queue_declare('steps')

# # Start consuming messages
# rabbit.receive()
# rabbit.start_consuming()

rabbit.send('steps', 'Tapioca!')

rabbit.connectionClose()