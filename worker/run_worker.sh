celery -A broadcast_test worker -l debug -n worker1@kudu
celery -A broadcast_test worker -l debug -n worker2@kudu
