import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    time.sleep(0.5)
    print(" [x] Received %r" % str(body,encoding='utf8'))
    time.sleep(body.count(b'.'))
    print(" [x] Done")

channel.basic_consume(callback,queue='hello',no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
