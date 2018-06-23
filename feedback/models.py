from django.db import models
from django.conf import settings


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    subject = models.TextField()
    feedtext = models.TextField()
    phone = models.BigIntegerField()
