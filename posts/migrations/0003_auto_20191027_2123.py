# Generated by Django 2.0.7 on 2019-10-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191026_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Время прочтения'),
        ),
    ]
