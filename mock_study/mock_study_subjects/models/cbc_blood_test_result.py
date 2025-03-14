from django.db import models
from django.utils import timezone
from ..choices import TESTING_SITES, TESTING_STATUS


class CBCBloodTestResult(models.Model):

    subject_identifier = models.CharField(max_length=20)

    sample_id = models.CharField(max_length=10)

    red_blood_cell_count = models.FloatField()

    hemoglobin = models.FloatField()

    hematocrit = models.FloatField()

    white_blood_cell_count = models.FloatField()

    platelet_count = models.FloatField()

    date_tested = models.DateField(default=timezone.now())

    test_site = models.CharField(max_length=50, choices=TESTING_SITES)

    testing_status = models.CharField(max_length=10, choices=TESTING_STATUS)

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'CBC Blood Test Result'
        verbose_name_plural = 'CBC Blood Test Results'
