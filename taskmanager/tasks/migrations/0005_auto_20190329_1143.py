# Generated by Django 2.1.7 on 2019-03-29 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20190329_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(blank=True, related_name='assignee_mem', to=settings.AUTH_USER_MODEL),
        ),
    ]
