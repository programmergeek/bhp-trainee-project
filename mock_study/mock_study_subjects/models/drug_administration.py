from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin


class DrugAdministration(CrfModelMixin):

    drug_taken = models.CharField(
        max_length=3,
        verbose_name="Has the the participant taken the drug?", choices=YES_NO)

    comment = models.TextField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = "Drug Administration"
        verbose_name_plural = "Drug Administration"
