# Generated by Django 2.2.1 on 2025-03-06 08:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0006_auto_20250306_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 6, 8, 59, 57, 456783, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
