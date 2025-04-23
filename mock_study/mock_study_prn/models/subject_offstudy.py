from django.db import models
from edc_base.model_mixins import BaseModel
from edc_base.sites import SiteModelMixin
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import SubjectIdentifierManager
from ..action_items.subject_offstudy_action_item import SUBJECT_OFF_STUDY_ACTION_ITEM_NAME


class SubjectOffStudy(SiteModelMixin, BaseModel, ActionModelMixin):

    action_name = SUBJECT_OFF_STUDY_ACTION_ITEM_NAME

    report_datetime = models.DateTimeField()

    reason = models.TextField()

    off_study_date = models.DateField()

    history = HistoricalRecords()

    objects = SubjectIdentifierManager()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = 'Subject Off Study'
        verbose_name_plural = "Subject Off Study"
