# Generated by Django 2.2.1 on 2025-03-14 06:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0042_auto_20250314_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adverseevent',
            name='onset_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 14, 6, 36, 33, 797772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cbcbloodtestresult',
            name='date_tested',
            field=models.DateField(default=datetime.datetime(2025, 3, 14, 6, 36, 33, 796718, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 14, 6, 36, 33, 788167, tzinfo=utc), verbose_name='Report date and time.'),
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 14, 6, 36, 33, 794581, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 14, 6, 36, 33, 788167, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
