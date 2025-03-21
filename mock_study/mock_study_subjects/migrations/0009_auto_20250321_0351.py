# Generated by Django 2.2.1 on 2025-03-21 03:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('mock_study_subjects', '0008_auto_20250320_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectscreening',
            name='site',
            field=models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='historicalsubjectscreening',
            name='slug',
            field=models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='subjectscreening',
            name='site',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='subjectscreening',
            name='slug',
            field=models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='onset_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 21, 3, 51, 0, 299547, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cbcbloodtestresult',
            name='date_tested',
            field=models.DateField(default=datetime.datetime(2025, 3, 21, 3, 51, 0, 298437, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 3, 51, 0, 44505, tzinfo=utc), verbose_name='Report date and time.'),
        ),
        migrations.AlterField(
            model_name='subjectbloodsample',
            name='collection_date',
            field=models.DateField(default=datetime.datetime(2025, 3, 21, 3, 51, 0, 296181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='report_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 3, 51, 0, 44505, tzinfo=utc), verbose_name='Report date and time.'),
        ),
    ]
