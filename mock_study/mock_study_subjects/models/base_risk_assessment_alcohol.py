from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin


class BaseRiskAssessmentAlcohol(CrfModelMixin):

    consumes_alcohol = models.CharField(max_length=3, choices=YES_NO , verbose_name='Do you drink alcohol?')

    drinks_per_week = models.IntegerField(verbose_name='How many days per week do you consume alcohol?', validators=[MinValueValidator(1), MaxValueValidator(7)], blank=True, null=True)

    amount_of_drinks = models.IntegerField(verbose_name='When you do drink, how many drinks do you normally have?', validators=[MinValueValidator(1), MaxValueValidator(30)], blank=True, null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Alcohol'
        verbose_name_plural = 'Base Risk Assessment: Alcohol'
