# Generated by Django 2.1.7 on 2019-03-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('desc', models.CharField(max_length=256)),
                ('assignee', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
