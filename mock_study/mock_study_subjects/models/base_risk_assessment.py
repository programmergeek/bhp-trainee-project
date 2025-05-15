from django.db import models

from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin

class BaseRiskAssessment(CrfModelMixin):

    drinks_alcohol = models.CharField(max_length=3, verbose_name='Do you drink alcohol?', choices=YES_NO)

    drinks_caffeine = models.CharField(max_length=3, verbose_name='Do you drink caffinated drinks?', choices=YES_NO)

    class Meta(CrfModelMixin.Meta):
        app_label='mock_study_subjects'
        verbose_name = 'Base Risk Assessment'
        verbose_name_plural = 'Base Risk Assessment'
