from ..constants import GENDER
from django.db import models
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin

"""
NOTES: 

 - UpdatesOrCreatesRegistrationModelMixin: handles registering a participant
"""


class SubjectConsent(models.Model):

    subject_screening_model = 'mock_study_subjects.subject_screening'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        null=True,
        blank=True,
        max_length=50)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1,
        null=True,
        blank=False)

    is_signed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'mock_study_subjects'
        get_latest_by = 'consent_datetime'
        verbose_name = 'Mock Study Consent'
        verbose_name_plural = 'Mock Study Consent'
