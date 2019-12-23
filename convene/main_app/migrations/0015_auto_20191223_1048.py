# Generated by Django 3.0 on 2019-12-23 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20191223_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='users',
        ),
        migrations.AddField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='main_app.Event'),
            preserve_default=False,
        ),
    ]