from ..constants import GENDER
from django.db import models
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseModel
from edc_base.sites import SiteModelMixin
from edc_base.model_fields import OtherCharField
from edc_consent.field_mixins import (SampleCollectionFieldsMixin)
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin

from .mixins.search_slug_model_mixin import SearchSlugMixin
from ..choices import ID_TYPE
from .subject_screening import SubjectScreening

"""
NOTES:
 - UpdatesOrCreatesRegistrationModelMixin: handles registering a participant
 - A mixin is a reusable class that contains useful pieces of code I can use in different parts of my app.
"""


class ConsentManager(models.Manager):
    '''
    This function allows us to search for a subject's consent using their subject identifier and the version of the consent form
    '''

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(ConsentModelMixin,
                     UpdatesOrCreatesRegistrationModelMixin,
                     SiteModelMixin,
                     NonUniqueSubjectIdentifierModelMixin,
                     IdentityFieldsMixin,
                     ReviewFieldsMixin,
                     PersonalFieldsMixin,
                     SampleCollectionFieldsMixin,
                     VulnerabilityFieldsMixin,
                     SearchSlugMixin,
                     BaseModel):

    screening_identifier = models.ForeignKey(
        SubjectScreening, on_delete=models.CASCADE)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1,
        null=True,
        blank=False)

    identity_type = models.CharField(
        verbose_name="What type of identity number is this?",
        max_length=25,
        choices=ID_TYPE
    )

    other_idenity_type = OtherCharField()

    is_signed = models.BooleanField(default=False, editable=False)

    consent = SubjectConsentManager()

    objects = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    def schedule_name(self):
        return 'mock_study_schedule'

    class Meta(ConsentModelMixin.Meta):
        app_label = 'mock_study_subjects'
        get_latest_by = 'consent_datetime'
        verbose_name = 'Mock Study Consent'
        verbose_name_plural = 'Mock Study Consent'
