from django.db import models
from edc_constants.choices import YES_NO_DONT_KNOW

from .mixins.crfs_model_mixin import CrfModelMixin

class BaseRiskAssessmentFamily(CrfModelMixin):

    direct_family = models.CharField(max_length=15, choices=YES_NO_DONT_KNOW, verbose_name='Have your parents or grandparents ever been diagnosed with hypertension?')

    extended_family = models.CharField(max_length=15, choices=YES_NO_DONT_KNOW, verbose_name='Have any members of your extended family, for example cousins, aunts, or uncles, ever been diagnosed with hypertension?')

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Family'
        verbose_name_plural = 'Base Risk Assessment: Family'
