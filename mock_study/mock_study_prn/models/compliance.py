from django.db import models
from django.utils import timezone
from edc_base.model_mixins import BaseModel
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import SubjectIdentifierManager
from edc_action_item.model_mixins import ActionModelMixin
from ..action_items.complaince_action_item import COMPLIANCE_ACTION_ITEM_NAME


class ComplianceReport(BaseModel, ActionModelMixin):

    action_name = COMPLIANCE_ACTION_ITEM_NAME

    doses_prescribed = models.IntegerField(default=0)

    doses_taken = models.IntegerField(default=0)

    missed_dosses_reason = models.TextField(
        blank=True,
        null=True,
        verbose_name="If you have not taken the prescribed dossage please explain why?",
    )

    missed_visits = models.IntegerField()

    report_datetime = models.DateTimeField(
        verbose_name="Amount of visits missed",
        default=timezone.now()
    )

    comment = models.TextField()

    history = HistoricalRecords()

    objects = SubjectIdentifierManager()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = 'Compliance Report'
        verbose_name_plural = 'Compliance Reports'
