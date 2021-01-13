#!/usr/bin/env python
import pika, sys, os

# Code based on RabbitMQ basic tutorial:
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

class RabbitMQ:

    """This Class handles sending and receing data with RabbitMQ."""

    def __init__(self):
        self.connection = None
        self.channel = None


    def connection_rabbitmq(self):
        print('Connecting to RabbitMQ Server...')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # Establish a connection with RabbitMQ server.
        self.channel = self.connection.channel()
        print('Connected to RabbitMQ Server')


    def queue_declare(self, queue):
        self.channel.queue_declare(queue=queue)


    def send(self, queue, message):
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)


    def connectionClose(self):
        self.connection.close()
        print('RabbitMQ connection closed.')

    
    # ----------------------------------------------------- #
    # IMPLEMETNTATIONS NOT NECESSARY (RECEIVE MODE ONLY)    #
    # ----------------------------------------------------- #


    # def callback(ch, method, properties, body):
    #     print(" [x] Received %r" % body)


    # def receive(self, queue):
    #     def callback(ch, method, properties, body):
    #         print(" [x] Received %r" % body)
    #     self.channel.basic_consume(queue=queue, auto_ack=True, on_message_callback=callback)


    # def start_consuming(self):
    #     print('Starting cosumming...')
    #     self.channel.start_consuming()


