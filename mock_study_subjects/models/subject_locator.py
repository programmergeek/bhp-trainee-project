from django.contrib.sites.models import Site
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django_crypto_fields.fields import EncryptedCharField
from ..choices import YES_NO


class SubjectLocator(models.Model):

    tracking_identifier_prefix = 'SL'

    site = models.ForeignKey(
        Site, on_delete=models.PROTECT, null=True, editable=False,
        related_name='subject_locator_site')

    date_signed = models.DateField(
        verbose_name="Date Locator Form signed ",
        default=timezone.now,
        help_text="",
    )

    local_clinic = models.CharField(
        verbose_name=(
            "When you stay in the village, what clinic/health post do you normally go to?"),
        max_length=75,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}[-][0-9]{1}[-][0-9]{2}$',
            message='The correct clinic code format is XX-X-XX'), ],
        help_text="Please give clinic code.",
    )
    home_village = models.CharField(
        verbose_name=("Where is your home village?"),
        max_length=75,
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

    def __str__(self):
        return '{}'.format(self.subject_identifier)

    def natural_key(self):
        return (self.subject_identifier, )
    natural_key.dependencies = ['sites.Site']

    class Meta:
        verbose_name = 'Subject Locator'
        verbose_name_plural = 'Subject Locator'
