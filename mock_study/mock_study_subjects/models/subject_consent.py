from ..constants import GENDER
from django.db import models
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin as BaseUpdatesOrCreatesRegistrationModelMixin
from edc_base.constants import DEFAULT_BASE_FIELDS
from django.core.exceptions import ImproperlyConfigured
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.field_mixins import (SampleCollectionFieldsMixin,
                                      CitizenFieldsMixin)
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin)

"""
NOTES:
 - UpdatesOrCreatesRegistrationModelMixin: handles registering a participant
"""


class ConsentManager(models.Manager):

    '''
    This function allows us to search for a subject's consent using their subject identifier and the version of the consent form
    '''

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)

# A mixin is a reusable class that contains useful pieces of code I can use in different parts of my app.


class updatesOrCreatesRegistrationMixin(BaseUpdatesOrCreatesRegistrationModelMixin):

    # This is a property inherited from the super class
    # It returns the attribute that will update registered_subject_unique_field
    @property
    def registration_unique_field(self):
        return 'subject_identifier'

    # gets values for attributes that are shared between the registration model and this instance
    @property
    def registration_options(self):
        registration_options = {}
        for field in self.registration_model._meta.get_fields():
            # _state is an internal value used by django to track the lifecycle of the model instance
            if (field.name not in DEFAULT_BASE_FIELDS + ['_state']
                    + [self.registration_unique_field]):
                try:
                    registration_options.update({field.name: getattr(
                        self, field.name)})
                except AttributeError:
                    pass
        return registration_options

    def registration_raise_on_not_unique(self):
        '''
        This field check if the value of registration_identifier is unique.
        registration_identifier is equal to the return value of
        registration_unique_field which is subject_identifier
        '''

        unique_fields = ['registration_identifier']
        for f in self.registration_model._meta.get_fields():
            try:
                if f.unique:
                    unique_fields.append(f.name)
            except AttributeError:
                pass
        if self.registration_unique_field not in unique_fields:
            raise ImproperlyConfigured(
                'Field is not unique. Got {}-- {}'.format(
                    self._meta.label_lower, self.registration_unique_field))

    class Meta:
        # Defines this mixin as an abstract model, meaning only the models which implement this mixin
        # have tables created for them in the database, but the mixin won't get a table
        abstract = True


class SubjectConsent(ConsentModelMixin,  # contains common properties for consent models
                     # keeps track of which site the consent is giver and the particpant is registered
                     SiteModelMixin,
                     # contains logic to register participant
                     UpdatesOrCreatesRegistrationModelMixin,
                     # Creating a subject identifier and using that as
                     # creates a unique subject identifier field and its corresponding methods
                     NonUniqueSubjectIdentifierModelMixin,
                     IdentityFieldsMixin,  # fields related to persons identity e.g id number
                     ReviewFieldsMixin,  # Review questions
                     PersonalFieldsMixin,
                     SampleCollectionFieldsMixin,
                     # Fields relating to a person's citizenship status or if they are married to citizen.
                     CitizenFieldsMixin,
                     VulnerabilityFieldsMixin,
                     BaseUuidModel):

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

    consent = SubjectConsentManager()

    objects = ConsentManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    class Meta:
        app_label = 'mock_study_subjects'
        get_latest_by = 'consent_datetime'
        verbose_name = 'Mock Study Consent'
        verbose_name_plural = 'Mock Study Consent'
