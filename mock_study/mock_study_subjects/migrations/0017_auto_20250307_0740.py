# Generated by Django 2.2.1 on 2025-03-07 07:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0016_enrollmentmanager_subjectscreening'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectConsent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screening_identifier', models.CharField(blank=True, max_length=50, null=True, verbose_name='Screening identifier')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('is_signed', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'get_latest_by': 'consent_datetime',
            },
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 7, 7, 40, 48, 832934, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
