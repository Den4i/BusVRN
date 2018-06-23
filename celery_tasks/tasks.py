from celery_tasks.celery_app import app
from django.core.mail import send_mail


@app.task
def send_feedback_email_task(subject, feedtext, from_email, to_email):
    return send_mail(subject, feedtext, from_email, to_email)
