from django.db import models

from edc_base.model_validators.date import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start

from .mixins.crfs_model_mixin import CrfModelMixin

class DrugResponse(CrfModelMixin):

    drug_response = models.TextField(verbose_name='Briefly describe the participant\'s response to the drug and the information used to judge the response.')

    response_datetime = models.DateTimeField(verbose_name='Date of the response assessment.', validators=[datetime_not_future, datetime_not_before_study_start])

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Response to Drug'
        verbose_name_plural = 'Response to Drug'
