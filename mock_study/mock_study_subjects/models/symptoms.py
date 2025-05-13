from django.db import models

from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin

class Symptoms(CrfModelMixin):

    headache = models.CharField(verbose_name="Do you have severe headaches?", choices=YES_NO, max_length=3)
    chest_pain = models.CharField(verbose_name='Do have any chest pains?', choices=YES_NO, max_length=3)
    dizziness = models.CharField(verbose_name="Have you been feeling dizzy recently?", choices=YES_NO, max_length=3)
    breathing = models.CharField(verbose_name="Do have difficulty breathing?", choices=YES_NO, max_length=3)
    nausea = models.CharField(verbose_name="Have you been feeling nauseous recently?", choices=YES_NO, max_length=3)
    vomiting = models.CharField(verbose_name="Have you vommited recently?", choices=YES_NO, max_length=3)
    blurry_vision = models.CharField(verbose_name="Do you have blurry vision or have episodes of blurry vision?", choices=YES_NO, max_length=3)
    anxiety = models.CharField(verbose_name="Do you feel more anxious than normal", choices=YES_NO, max_length=3)
    abnomal_heart_rhythm = models.CharField(verbose_name="Have you been experiencing abnormal heart beats?", choices=YES_NO, max_length=3)
    other_symtoms = models.TextField(verbose_name="Are there any other symptoms you have been exepriencing that are not listed above? If so please list them", blank=True, null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Symptoms'
        verbose_name_plural = 'Symptoms'
