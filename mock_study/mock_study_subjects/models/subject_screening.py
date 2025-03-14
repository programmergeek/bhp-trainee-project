from django.db import models
from django.utils import timezone

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords

from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin

from ..choices import YES_NO, ENROLLMENT_SITES
from ..screening_identifier import ScreeningIdentifier
from ..eligibility import Eligibility
import random
from math import floor


"""TODO: Hide some fields (hypertension diagnosis, pregnancy, etc.) until consent is provided.
"""

"""
NOTES: 

 - UniqueSubjectIdentifierFieldMixin: adds a subject_identifier field to your model
 - BaseUuidModel: changes the id field from an int to a uuid and providing extra fields such as when record was created created 
 - Managers allow your models to communicate with the database. EnrollmentManager extends the django manager class to add the function get_by_natural_keys
"""


class EnrollmentManager(models.Manager):
    """
    get_by_natural_key allows us to search for patients using their screening identifier.
    """

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class SubjectScreening(UniqueSubjectIdentifierFieldMixin, BaseUuidModel):

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
        verbose_name = 'Mock Study Eligibility'
        verbose_name_plural = 'Mock Study Eligibility'
