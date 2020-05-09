from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu.common import Broadcast
app = Celery('broadcast_test',
             broker='amqp://',
             backend='rpc://',
             include=['broadcast_test.tasks'])
app.conf.task_queues = (Broadcast('broadcast_tasks'),)
app.conf.task_routes = {'tasks.add': {'queue': 'broadcast_tasks'}}
if __name__ == '__main__':
    app.start()
