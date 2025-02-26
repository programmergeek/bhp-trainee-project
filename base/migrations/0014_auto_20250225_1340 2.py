# Generated by Django 2.2.1 on 2025-02-25 13:40

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20250225_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodsample',
            name='collection_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 25, 13, 40, 44, 885041, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='participantvital',
            name='weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(500.0)]),
        ),
    ]
