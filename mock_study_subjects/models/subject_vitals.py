from django.db import models
from ..choices import YES_NO, ENROLLMENT_SITES


class SubjectVitals(models.Model):

    subject_identifier = models.CharField(max_length=10)

    collection_site = models.CharField(max_length=50, choices=ENROLLMENT_SITES)

    were_vitals_collected = models.CharField(max_length=3, choices=YES_NO)

    measurement_date = models.DateField()

    systolic_blood_pressure = models.IntegerField()

    diastolic_blood_pressure = models.IntegerField()

    anatomical_location_of_measurement = models.CharField(max_length=50)

    height = models.FloatField()

    weight = models.FloatField()

    is_baseline = models.BooleanField(
        verbose_name='Is this the participant\'s baseline vitals measurement?')

    class Meta:
        app_label = "mock_study_subjects"
        verbose_name = "Subject Vitals"
        verbose_name_plural = 'Subject Vitals'
