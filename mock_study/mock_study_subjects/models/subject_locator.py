from django.db import models
from django.utils import timezone
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_locator.model_mixins import LocatorModelMixin, LocatorManager


class SubjectLocator(LocatorModelMixin, RequiresConsentFieldsModelMixin, BaseUuidModel):

    date_signed = models.DateField(
        verbose_name="Date Locator Form signed ",
        default=timezone.now,
        help_text="",
    )

    history = HistoricalRecords()

    objects = LocatorManager()

    def __str__(self):
        return '{}'.format(self.subject_identifier)

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Subject Locator'
        verbose_name_plural = 'Subject Locator'
