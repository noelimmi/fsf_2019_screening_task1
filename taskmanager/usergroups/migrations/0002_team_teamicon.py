# Generated by Django 2.1.7 on 2019-03-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usergroups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='teamicon',
            field=models.ImageField(default='groupdefault.png', upload_to='group_icons'),
        ),
    ]