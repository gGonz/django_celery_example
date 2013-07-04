import time
from celery import task, current_task


@task
def count_to_number_sleeping(count_to=0):
    """
    A very basic and useless Celery task example.

    """
    # Looping
    for n in xrange(1, count_to + 1):
        # Updates the task status to show a more informative state and add
        # the information of the current step of the task and the total
        # steps, this way we can do an approach of the progress of the task
        # in the client side.
        current_task.update_state(
            state='WORKING',
            meta={'counted': n, 'of': count_to}
        )

        # Sleeping
        time.sleep(1)

    # Returns the result of the task
    return n
