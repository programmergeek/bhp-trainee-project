from django.db import models
from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin

class BaseRiskAssessmentHealth(CrfModelMixin):

    medication = models.CharField(max_length=3, choices=YES_NO, verbose_name="Are you currently using any prescribed medication?")

    reason_for_medication = models.TextField(verbose_name='If you are, what is meant to treat?', blank=True, null=True)

    side_effects = models.CharField(max_length=3, blank=True, null=True, verbose_name='Does the medication have increased blood pressure as a side effect?')

    heart_attack = models.CharField(max_length=3, verbose_name="Have you ever had a heart attack?", choices=YES_NO)

    aneurysm = models.CharField(max_length=3, verbose_name='Have you ever had an aneurysm?', choices=YES_NO)

    stroke = models.CharField(max_length=3, verbose_name="Have you ever had a stroke?", choices=YES_NO)

    kidney_disease = models.CharField(max_length=3, verbose_name='Have you ever had kidney disease?', choices=YES_NO)

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Health'
        verbose_name_plural = 'Base Risk Assessment: Health'
