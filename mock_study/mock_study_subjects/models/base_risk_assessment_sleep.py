from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin
from ..choices import RATING_SCALE


class BaseRiskAssessmentSleep(CrfModelMixin):

    sleep = models.CharField(max_length=20, verbose_name='Do you normally get a full night\'s rest?', choices=RATING_SCALE)

    restlessness = models.CharField(max_length=20, verbose_name='Do you normally wakeup a lot when you go to bed?', choices=RATING_SCALE)

    night_shift = models.CharField(max_length=3, verbose_name='Do you work nights?', choices=YES_NO)

    hours_slept = models.IntegerField(verbose_name="How many hours of sleep do you normally get?", validators=[MinValueValidator(1), MaxValueValidator(24)])

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Sleep'
        verbose_name_plural = 'Base Risk Assessment: Sleep'
