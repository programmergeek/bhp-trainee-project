from django.contrib.sites.models import Site
from django.db import models
from django.utils import timezone
from ..choices import YES_NO
from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager, SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_locator.model_mixins import LocatorModelMixin, LocatorManager


class SubjectLocator(LocatorModelMixin, RequiresConsentFieldsModelMixin, SiteModelMixin, BaseUuidModel):

    site = models.ForeignKey(
        Site, on_delete=models.PROTECT, null=True, editable=False,
        related_name='subject_locator_site')

    date_signed = models.DateField(
        verbose_name="Date Locator Form signed ",
        default=timezone.now,
        help_text="",
    )

    has_alt_contact = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=("If we are unable to contact the person indicated above, is there another"
                      " individual (including next of kin) with whom the study team can get"
                      " in contact with?"),
        help_text="",
    )

    alt_contact_name = EncryptedCharField(
        max_length=35,
        verbose_name="Full Name of the responsible person",
        help_text="include firstname and surname",
        blank=True,
        null=True,
    )

    alt_contact_rel = EncryptedCharField(
        max_length=35,
        verbose_name="Relationship to participant",
        blank=True,
        null=True,
        help_text="",
    )
    alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number",
        help_text="",
        blank=True,
        null=True,
    )

    other_alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number (alternate)",
        help_text="",
        blank=True,
        null=True,
    )

    alt_contact_tel = EncryptedCharField(
        max_length=8,
        verbose_name="Telephone number",
        help_text="",
        blank=True,
        null=True,
    )

    history = HistoricalRecords()

    objects = LocatorManager()

    on_site = CurrentSiteManager()

    def __str__(self):
        return '{}'.format(self.subject_identifier)

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Subject Locator'
        verbose_name_plural = 'Subject Locator'
