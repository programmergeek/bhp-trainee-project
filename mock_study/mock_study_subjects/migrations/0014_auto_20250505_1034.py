# Generated by Django 2.2.1 on 2025-05-05 08:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0013_auto_20250505_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adverseevent',
            name='onset_date',
            field=models.DateField(default=datetime.datetime(2025, 5, 5, 8, 34, 5, 278713, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cbcbloodtestresult',
            name='date_tested',
            field=models.DateField(default=datetime.datetime(2025, 5, 5, 8, 34, 5, 277455, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 5, 8, 34, 5, 261261, tzinfo=utc), verbose_name='Report date and time.'),
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 5, 5, 8, 34, 5, 275343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 5, 8, 34, 5, 261261, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
