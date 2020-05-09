import broadcast_test.tasks 
broadcast_test.tasks.add.apply_async((2, 2), queue='broadcast_tasks')
