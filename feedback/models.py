from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, verbose_name='Пользователь')
    subject = models.TextField(verbose_name='Тема')
    feedtext = models.TextField(verbose_name='Текст')
    phone = PhoneNumberField(verbose_name='Телефон')

    class Meta:
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return "%s/%s" % (self.user, self.subject)
