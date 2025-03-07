from ..constants import DEFAULT_BASE_FIELDS, GENDER
from django.core.exceptions import ImproperlyConfigured
from django.db import models


class ConsentManager():

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)

#
# class UpdatesOrCreatesRegistrationModelMixin():
#
#     @property
#     def registration_unique_field(self):
#         return 'subject_identifier'
#
#     @property
#     def registration_options(self):
#         """Gathers values for common attributes between the
#         registration model and this instance.
#         """
#         registration_options = {}
#         for field in self.registration_model._meta.get_fields():
#             if (field.name not in DEFAULT_BASE_FIELDS + ['_state']
#                     + [self.registration_unique_field]):
#                 try:
#                     registration_options.update({field.name: getattr(
#                         self, field.name)})
#                 except AttributeError:
#                     pass
#         return registration_options
#
#     def registration_raise_on_not_unique(self):
#         """Asserts the field specified for update_or_create is unique.
#         """
#         unique_fields = ['registration_identifier']
#         for f in self.registration_model._meta.get_fields():
#             try:
#                 if f.unique:
#                     unique_fields.append(f.name)
#             except AttributeError:
#                 pass
#         if self.registration_unique_field not in unique_fields:
#             raise ImproperlyConfigured(
#                 'Field is not unique. Got {}.{} -- {}'.format(
#                     self._meta.label_lower, self.registration_unique_field))
#
#     class Meta:
#         abstract = True


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

    objects = ConsentManager()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['identity', 'screening_identifier',
                       'first_name', 'last_name'])
        return fields

    def make_new_identifier(self):
        """Returns a new and unique identifier.

        Override this if needed.
        """
        pass

    class Meta:
        app_label = 'mock_study_subjects'
        get_latest_by = 'consent_datetime'
        verbose_name = 'Mock Study Consent'
        verbose_name_plural = 'Mock Study Consent'
