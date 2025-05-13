from django.db import models

from .mixins.crfs_model_mixin import CrfModelMixin
from ..choices import RATING_SCALE

class BaseRiskAssessmentStress(CrfModelMixin):

    work_stress = models.CharField(max_length=30, verbose_name="Would you describe your job as stressful?", choices=RATING_SCALE)

    home_stress = models.CharField(max_length=30, verbose_name='Would you descibe your home life as stressful?', choices=RATING_SCALE)

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Stress'
        verbose_name_plural = 'Base Risk Assessment: Stress'
