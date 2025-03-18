from django.db import models
from .mixins.crfs_model_mixin import CrfModelMixin


class SubjectVitals(CrfModelMixin):
    systolic_blood_pressure = models.IntegerField(
        help_text='mmHg'
    )

    diastolic_blood_pressure = models.IntegerField(
        help_text='mmHg'
    )

    heart_rate = models.IntegerField(help_text='bpm')

    height = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        help_text='cm'
    )

    weight = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        help_text='kg'
    )

    class Meta:
        app_label = "mock_study_subjects"
        verbose_name = "Subject Vitals"
        verbose_name_plural = 'Subject Vitals'
