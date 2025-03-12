# Generated by Django 2.2.1 on 2025-03-12 10:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0029_auto_20250312_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adverseevent',
            options={'verbose_name': 'Adverse Event', 'verbose_name_plural': 'Adverse Events'},
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 12, 10, 27, 29, 683989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 12, 10, 27, 29, 674044, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
