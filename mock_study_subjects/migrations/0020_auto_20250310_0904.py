# Generated by Django 2.2.1 on 2025-03-10 09:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0019_auto_20250310_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 10, 9, 4, 14, 773832, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
