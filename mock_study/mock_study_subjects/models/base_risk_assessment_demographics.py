from django.db import models

from edc_constants.choices import YES_NO
from edc_base.model_fields import OtherCharField

from .mixins.crfs_model_mixin import CrfModelMixin
from ..choices import MARITAL_STATUS, RACE, EDUCATION


class BaseRiskAssessmentDemographics(CrfModelMixin):

    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)

    marital_status_other = OtherCharField(max_length=20, blank=True, null=True, verbose_name="If you selected 'Other', please enter your marital status.")

    race = models.CharField(max_length=10, choices=RACE)

    race_other = OtherCharField(max_length=10, blank=True, null=True, verbose_name="If you selected 'Other, please enter your race.'")

    employed = models.CharField(max_length=3, verbose_name='Are you currently employed?', choices=YES_NO)

    education = models.CharField(max_length=30, verbose_name='What is the highest level of education you have?', choices=EDUCATION)

    education_other = OtherCharField(max_length=50, blank=True, null=True, verbose_name="If you selected 'Other', please enter your level of education.")

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Demographics'
        verbose_name_plural = 'Base Risk Assessment: Demographics'
