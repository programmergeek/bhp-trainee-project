# Generated by Django 2.2.1 on 2025-02-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20250224_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalquestionnaire',
            name='participant_experience',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='finalquestionnaire',
            name='perceived_benefits',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='finalquestionnaire',
            name='perceived_challenges',
            field=models.TextField(max_length=500),
        ),
    ]
