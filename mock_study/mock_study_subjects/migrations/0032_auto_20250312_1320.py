# Generated by Django 2.2.1 on 2025-03-12 13:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0031_auto_20250312_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExitInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_identifier', models.CharField(max_length=20)),
                ('summary', models.TextField()),
                ('investigator_observation', models.TextField()),
                ('final_comments', models.TextField()),
                ('final_recommendation', models.TextField()),
            ],
            options={
                'verbose_name': 'Exit Interview',
                'verbose_name_plural': 'Exit Interviews',
            },
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 12, 13, 20, 25, 303685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 12, 13, 20, 25, 292058, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
