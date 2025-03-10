from ..constants import GENDER
from django.core.exceptions import ImproperlyConfigured
from django.db import models


class SubjectConsent(models.Model):
    """ A model completed by the user that captures the ICF.
    """
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

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['identity', 'screening_identifier',
                       'first_name', 'last_name'])
        return fields

    class Meta:
        app_label = 'mock_study_subjects'
        get_latest_by = 'consent_datetime'
        verbose_name = 'Mock Study Consent'
        verbose_name_plural = 'Mock Study Consent'
