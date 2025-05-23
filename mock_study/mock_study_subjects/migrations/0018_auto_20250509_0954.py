# Generated by Django 2.2.1 on 2025-05-09 07:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0017_auto_20250508_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adverseevent',
            name='onset_date',
            field=models.DateField(default=datetime.datetime(2025, 5, 9, 7, 54, 16, 390736, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cbcbloodtestresult',
            name='date_tested',
            field=models.DateField(default=datetime.datetime(2025, 5, 9, 7, 54, 16, 390153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='is_breastfeeding',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text="If 'Yes', then stop. The patient cannot be part of this study.", max_length=3, null=True, verbose_name='Is the patient currently breastfeeding?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='is_pregnant',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text="If 'Yes', then stop. The patient cannot be part of this study. ", max_length=3, null=True, verbose_name='Are they currently pregnant?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 9, 7, 54, 16, 380403, tzinfo=utc), verbose_name='Report date and time.'),
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 5, 9, 7, 54, 16, 388597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='is_breastfeeding',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text="If 'Yes', then stop. The patient cannot be part of this study.", max_length=3, null=True, verbose_name='Is the patient currently breastfeeding?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='is_pregnant',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text="If 'Yes', then stop. The patient cannot be part of this study. ", max_length=3, null=True, verbose_name='Are they currently pregnant?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 9, 7, 54, 16, 380403, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
