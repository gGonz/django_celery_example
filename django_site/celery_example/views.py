import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView

from celery_example.tasks import count_to_number_sleeping


class ExampleView(TemplateView):
    template_name = 'example.html'

    def post(self, request, *args, **kwargs):
        # Calling the Celery task with its "delay" method. We tell Celery
        # to execute the task on the background, Celery pushes the task to
        # the queue and returns a task object. A task is identified by a
        # v4 UUID.
        task = count_to_number_sleeping.delay(int(request.POST['count_to']))

        # Returns a custom JSON object that only contains the url where we
        # can check the status of the task.
        return HttpResponse(json.dumps({
            'task_url': reverse('status', kwargs={
                'task_id': task.task_id}
            )
        }))
