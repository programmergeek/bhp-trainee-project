# Generated by Django 2.2.1 on 2025-03-06 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0005_auto_20250306_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 6, 8, 4, 13, 842764, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
