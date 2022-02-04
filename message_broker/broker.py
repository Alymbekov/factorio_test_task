from typing import Optional

import pika
from loguru import logger
from decouple import config


class MessageBroker:
    credentials = pika.PlainCredentials(config("RMQ_USER"), config("RMQ_PWD"))
    params = pika.ConnectionParameters(host=config("RMQ_HOST"),
                                       port=config("RMQ_PORT"),
                                       heartbeat=int(config("RMQ_HEARTBEAT")),
                                       credentials=credentials,
                                       blocked_connection_timeout=int(config("RMQ_CONNECTION_TIMEOUT")))

    def __init__(self, queue_name: str, max_priority: int = 10):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, arguments={'x-max-priority': max_priority})
        self.channel.basic_qos(prefetch_count=1)

        logger.debug(f'Established connection to rabbitMQ. Declared queue [{queue_name}] with priority {max_priority}')

    @staticmethod
    def _encode_message(message: str) -> Optional[bytes]:
        try:
            encoded_message = message.encode('utf-8', errors='strict')
            return encoded_message
        except UnicodeDecodeError:
            logger.error('Message encoding failed')
            return None

    def produce_message(self, message: str, priority: int = 1):
        encoded_message = self._encode_message(message)
        if encoded_message:
            properties = pika.BasicProperties(priority=priority, delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
            self.channel.basic_publish(exchange='',
                                       properties=properties,
                                       routing_key=self.queue_name,
                                       body=encoded_message)
            logger.info(f"Message was sent to queue")
        else:
            logger.error(f"Message {message} was skipped because of some issues with encoding")

    def consume_messages(self):
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=self.callback,
                                   auto_ack=False)
        logger.info('Start receiving tasks')
        self.channel.start_consuming()

    @staticmethod
    def callback(channel, method, properties, body):
        """
        Don't forget to use 'ch.basic_ack(delivery_tag=method.delivery_tag)' for manual ack of done tasks
        :return:
        """
        raise NotImplementedError
