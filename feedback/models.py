from django.db import models
from django.conf import settings


class FeedbackModel(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	feedtext = models.TextField()
	phone = models.BigIntegerField()