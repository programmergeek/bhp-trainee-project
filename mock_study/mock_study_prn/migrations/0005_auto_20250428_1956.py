# Generated by Django 2.2.1 on 2025-04-28 17:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_prn', '0004_auto_20250425_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalquestionnaire',
            name='respectful_staff_comment',
            field=models.TextField(blank=True, null=True, verbose_name='If you believe that the staff have not been respectful, please leave a comment as to why.'),
        ),
        migrations.AddField(
            model_name='historicalfinalquestionnaire',
            name='respectful_staff_comment',
            field=models.TextField(blank=True, null=True, verbose_name='If you believe that the staff have not been respectful, please leave a comment as to why.'),
        ),
        migrations.AlterField(
            model_name='compliancereport',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 28, 17, 56, 2, 348216, tzinfo=utc), verbose_name='Amount of visits missed'),
        ),
        migrations.AlterField(
            model_name='historicalcompliancereport',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 28, 17, 56, 2, 348216, tzinfo=utc), verbose_name='Amount of visits missed'),
        ),
    ]
