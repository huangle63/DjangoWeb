from __future__ import absolute_import, unicode_literals
from celery import task
import time

@task
def build_job(job_name, *kwargs):
    print(job_name)
    time.sleep(10)
    for item in kwargs:
        print(item)

    return None