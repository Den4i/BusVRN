# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import Celery

import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BusVRN.settings')

app = Celery('proj',
             broker='pyamqp://localhost',
             backend='redis://localhost'
             )

app.conf.update(
    result_expires=3600,
    task_routes={
        'celery_tasks.tasks.send_feedback_email_task': {'queue': 'high'},
    },
)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
