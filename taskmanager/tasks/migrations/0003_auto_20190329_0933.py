# Generated by Django 2.1.7 on 2019-03-29 04:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20190329_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamtask',
            name='assignee',
            field=models.ManyToManyField(related_name='assignedmem', to=settings.AUTH_USER_MODEL),
        ),
    ]