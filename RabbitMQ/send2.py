import pika
import datetime
import time

print(' [*] Waiting for messages. To exit press CTRL+C')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
count = 0
for i in range(100):
    now = datetime.datetime.now()
    now_str = now.strftime('%H:%M:%S')
    name = '__ send_②'+str(count)
    count += 1
    channel.basic_publish(exchange='',routing_key='hello',body=now_str+name)
    print("[x]Sent"+ now_str+name)
    time.sleep(0.1)
connection.close()