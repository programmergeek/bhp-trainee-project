from django.db import models
from django.utils import timezone
from ..choices import YES_NO


class EnrollementManager(models.Model):

    pass


ENROLLMENT_SITES = (
    ('gaborone_private_hospital', 'Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_Hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)


class SubjectScreening(models.Model):

    screening_identifier = models.CharField(
        max_length=36,
        verbose_name="Eligibility Identifier",
        unique=True,
        editable=False
    )

    report_datetime = models.DateTimeField(
        verbose_name='Report date and time.',
        default=timezone.now(),
    )

    has_hypertension = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Have they been diagnosed with hypertension?',
        help_text="If 'Yes', then stop. Patient cannot be part of the study."
    )

    eligible = models.BooleanField(
        default=False,
        editable=False
    )

    is_pregnant = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Are they currently pregnant?",
        help_text="If 'Yes', then stop. The patient cannot be part of this study. "
    )

    is_breastfeeding = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Is the patient currently breastfeeding?",
        help_text="If 'Yes', then stop. The patient cannot be part of this study."
    )

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospitals where subject is recruited."
    )

    def save(self, *args, **kwargs):

        pass

    def __str__(self):
        return f'{self.screening_identifier}'

    @property
    def schedule_name(self):
        return 'schedule'

    class Meta:
        app_label = 'mock_study_subject'
        verbose_name = 'Mock Study Eligibility'
        verbose_name_plural = 'Mock Study Eligibility'
