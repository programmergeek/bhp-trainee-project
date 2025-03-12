from django.db import models

from ..choices import ENROLLMENT_SITES


class Appointment(models.Model):

    subject_identifier = models.CharField(max_length=20)

    datetime = models.DateTimeField()

    site = models.CharField(max_length=20, choices=ENROLLMENT_SITES)

    class Meta():
        app_label = 'mock_study_subjects'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        pass
