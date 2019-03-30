# Generated by Django 2.1.7 on 2019-03-29 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usergroups', '0002_team_teamicon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_auto_20190329_0933'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teamtask',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='teamtask',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='teamtask',
            name='team',
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamtasks', to='usergroups.Team'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='teamtask',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskcomments', to='tasks.Task'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(null=True, related_name='assignee_mem', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Teamtask',
        ),
    ]
