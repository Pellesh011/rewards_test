# Generated by Django 5.2 on 2025-04-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0002_scheduledreward_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledreward',
            name='scheduled_time',
        ),
    ]
