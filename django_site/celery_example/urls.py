from django.conf.urls import patterns, url
from django.contrib import admin
from djcelery.views import task_status

from celery_example import views

admin.autodiscover()

urlpatterns = patterns('',
    # The main url of the site.
    url(r'^$',
        views.ExampleView.as_view(), name='example'
    ),
    # A custom url to check the status of a Celery task.
    url(r'^task/(?P<task_id>[\w\d\-\.]+)/status/$',
        task_status, name='status'
    ),
)
