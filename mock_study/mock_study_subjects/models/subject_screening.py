from django.db import models
from django.utils import timezone

from edc_base.model_mixins import BaseModel
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import GENDER, YES_NO

from .mixins.search_slug_model_mixin import ScreeningSearchSlugModelMixin

from ..choices import ENROLLMENT_SITES
from ..screening_identifier import ScreeningIdentifier
from ..eligibility import Eligibility


class EnrollmentManager(models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class SubjectScreening(
        ScreeningSearchSlugModelMixin,
        BaseModel):

    identifier_cls = ScreeningIdentifier
    eligibility_cls = Eligibility

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
        help_text="If 'No', then stop. Patient cannot be part of the study."
    )

    eligible = models.BooleanField(
        default=False,
        editable=False
    )

    age = models.IntegerField(
        help_text='If the patient is not between the ages of 30 and 65, then stop, they cannot be part of the study.'
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

    has_allergies_to_drug = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Does the patient have any known allergies to XYZ Drug?",
        help_text="If 'Yes', then stop. The patient cannot be part of this study."
    )

    has_history_of_severe_cardiovascular_events = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Does the patient have a history of sever cardiovascular events within the last 6 (six) months?",
        help_text="If 'Yes', then stop. The patient cannot be part of this study."

    )

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospitals where subject is recruited."
    )

    gender = models.CharField(
        max_length=2,
        null=True,
        choices=GENDER
    )

    history = HistoricalRecords()

    objects = EnrollmentManager()

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(
            hypertension_status=self.has_hypertension,
            has_history_of_severe_cardiovascular_events=self.has_history_of_severe_cardiovascular_events,
            has_allergies_to_drug=self.has_allergies_to_drug,
            is_breastfeeding=self.is_breastfeeding,
            age=self.age,
            is_pregnant=self.is_pregnant
        )
        self.eligible = eligibility_obj.eligible
        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.screening_identifier}'

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Mock Study Screening'
        verbose_name_plural = 'Mock Study Screening'
