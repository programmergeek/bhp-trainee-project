from django.db import models
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseModel
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import SubjectIdentifierManager
from edc_action_item.model_mixins import ActionModelMixin
from edc_constants.choices import YES_NO
from ..action_items.complaince_action_item import COMPLIANCE_ACTION_ITEM_NAME


class ComplianceReport(SiteModelMixin, BaseModel, ActionModelMixin):

    action_name = COMPLIANCE_ACTION_ITEM_NAME

    missed_days = models.TextField(
        verbose_name="How many times have you missed taking the study medication")

    doses_prescribed = models.IntegerField(default=0)

    doses_taken = models.IntegerField(default=0)

    has_side_effects = models.TextField(
        verbose_name="Has the participant noticied any side effects from the medication?", choices=YES_NO)

    side_effects = models.TextField(
        verbose_name="If 'Yes', describe what they are")

    comment = models.TextField()

    history = HistoricalRecords()

    objects = SubjectIdentifierManager()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = 'Compliance Report'
        verbose_name_plural = 'Compliance Reports'
