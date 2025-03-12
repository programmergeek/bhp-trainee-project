from django.db import models


class CBCBloodTestResult(models.Model):

    subject_identifier = models.CharField(max_length=20)

    sample_id = models.CharField(max_length=10)

    red_blood_cell_count = models.FloatField()

    hemoglobin = models.FloatField()

    hematocrit = models.FloatField()

    white_blood_cell_count = models.FloatField()

    platelet_count = models.FloatField()

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'CBC Blood Test Result'
        verbose_name_plural = 'CBC Blood Test Results'
