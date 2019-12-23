# Generated by Django 2.2.6 on 2019-12-23 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20191223_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='guests',
        ),
        migrations.AddField(
            model_name='guest',
            name='event',
            field=models.ManyToManyField(to='main_app.Event'),
        ),
    ]
