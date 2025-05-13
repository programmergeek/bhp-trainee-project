from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin

class BaseRiskAssessmentPhysicalActivity(CrfModelMixin):

    exercise = models.CharField(max_length=3, verbose_name='Do you execise regularly?', choices=YES_NO)

    days_per_week = models.IntegerField( blank=True, null=True, verbose_name='How many days per week do you execise?', validators=[MinValueValidator(1), MaxValueValidator(7)])

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Physical Activity'
        verbose_name_plural = 'Base Risk Assessment: Physical Activity'
