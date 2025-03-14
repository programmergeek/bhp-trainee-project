# Generated by Django 2.2.1 on 2025-03-12 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0026_auto_20250312_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 12, 8, 54, 45, 177934, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 12, 8, 54, 45, 164810, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
