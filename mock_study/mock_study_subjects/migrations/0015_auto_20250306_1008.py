# Generated by Django 2.2.1 on 2025-03-06 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mock_study_subjects', '0014_auto_20250306_0938'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EnrollmentManager',
        ),
        migrations.DeleteModel(
            name='SubjectScreening',
        ),
    ]
