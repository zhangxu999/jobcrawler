import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(method.delivery_tag)
    print(" [x] Received %r" % body)
    #time.sleep(body.count(b'.'))
    time.sleep(0.4)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=5)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
