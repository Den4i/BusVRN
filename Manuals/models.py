from django.db import models
from django.utils import timezone

# Create your models here.


class Route(models.Model):
    status = (
        (1, 'Active'),
        (0, 'Inactive')
    )
    name = models.CharField(max_length=5, verbose_name='Наименование')
    active = models.BooleanField(choices=status, verbose_name='Статус')

    def __str__(self):
        return 'Маршрут={0}   Статус={1}'.format(self.name, self.get_active_display())


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    routes = models.ManyToManyField(Route, through='ProjRouts')

    def __str__(self):
        return self.name


class ProjRouts(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Перевозчик')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Маршрут')

    def __str__(self):
        return 'Перевозчик={0},    {1}'.format(self.project, self.route)


class Object(models.Model):
    status = (
        (1, 'Выведен'),
        (0, 'Активен')
    )

    name = models.CharField(max_length=10, verbose_name='Гос. номер')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Перевозчик')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Маршрут')
    last_time = models.DateTimeField(verbose_name='Последнее время отклика', default=timezone.now)
    last_lat = models.FloatField(verbose_name='Широта', null=True, blank=True)
    last_lon = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    last_speed = models.IntegerField(verbose_name='Скорость', null=True, blank=True)
    phone = models.BigIntegerField(verbose_name='Телефон', null=True, blank=True)
    year_release = models.SmallIntegerField(verbose_name='Дата выпуска', null=True, blank=True)
    date_inserted = models.DateTimeField(verbose_name='Дата добавления', default=timezone.now)
    output = models.BooleanField(choices=status, verbose_name='Активность', default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0},   Перевозчик={1},  {2}'.format(self.name, self.project, self.route)
