from django.db import models
from django.utils import timezone

from ..choices import ENROLLMENT_SITES, TESTING_SITES, TESTING_STATUS, ANTICOAGULANTS


class SubjectBloodSample(models.Model):

    subject_identifier = models.CharField(max_length=20)

    sample_identifier = models.CharField(max_length=20)

    sample_type = models.CharField(max_length=10)

    collection_date = models.DateField(default=timezone.now())

    collected_by = models.CharField(max_length=20)

    collection_site = models.CharField(max_length=50, choices=ENROLLMENT_SITES)

    volume = models.FloatField()

    anticoagulant = models.CharField(max_length=50, choices=ANTICOAGULANTS)

    tube_type = models.CharField(max_length=50)

    storage_location = models.CharField(max_length=50, choices=TESTING_SITES)

    status = models.CharField(max_length=20, choices=TESTING_STATUS)

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Subject Blood Sample'
        verbose_name_plural = 'Subject Blood Samples'
