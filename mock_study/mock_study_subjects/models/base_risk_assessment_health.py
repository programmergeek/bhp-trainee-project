from django.db import models
from edc_constants.choices import YES_NO, YES_NO_DONT_KNOW

from .mixins.crfs_model_mixin import CrfModelMixin

class BaseRiskAssessmentHealth(CrfModelMixin):

    preexisting_condition_name = models.CharField(max_length=100, verbose_name="What is the name of your condition?")

    preexisting_condition_symptom = models.CharField(max_length=3, verbose_name='Is high blood pressure a symptom for this condition?')

    preexisting_condition_treatment = models.CharField(max_length=3, verbose_name='If yes, are you receiving any treatment for this condition?', choices=YES_NO)

    preexisting_condition_treatment_side_effects = models.CharField(max_length=20, verbose_name='Does this treatment list elevated/high blood pressure as a side effect?', choices=YES_NO_DONT_KNOW, blank=True, null=True)

    
    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Health'
        verbose_name_plural = 'Base Risk Assessment: Health'
