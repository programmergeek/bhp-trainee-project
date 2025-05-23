# Generated by Django 2.2.1 on 2025-04-14 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0007_auto_20250414_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adverseevent',
            name='onset_date',
            field=models.DateField(default=datetime.datetime(2025, 4, 14, 7, 10, 21, 170297, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cbcbloodtestresult',
            name='date_tested',
            field=models.DateField(default=datetime.datetime(2025, 4, 14, 7, 10, 21, 169188, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='is_breastfeeding',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', help_text="If 'Yes', then stop. The patient cannot be part of this study.", max_length=3, verbose_name='Is the patient currently breastfeeding?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='is_pregnant',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', help_text="If 'Yes', then stop. The patient cannot be part of this study. ", max_length=3, verbose_name='Are they currently pregnant?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 14, 7, 10, 20, 959681, tzinfo=utc), verbose_name='Report date and time.'),
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 4, 14, 7, 10, 21, 167204, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='is_breastfeeding',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', help_text="If 'Yes', then stop. The patient cannot be part of this study.", max_length=3, verbose_name='Is the patient currently breastfeeding?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='is_pregnant',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', help_text="If 'Yes', then stop. The patient cannot be part of this study. ", max_length=3, verbose_name='Are they currently pregnant?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 14, 7, 10, 20, 959681, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
