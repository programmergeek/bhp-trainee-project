from django.db import models
from django.utils import timezone
from edc_base.model_mixins import BaseModel
from edc_base.sites import SiteModelMixin
from edc_action_item.model_mixins import ActionModelMixin
from ..action_items.adverse_event_action_item import ADVERSE_EVENT_ACTION_NAME
from ..choices import SEVERITY


class AdverseEventActionModel(SiteModelMixin, BaseModel, ActionModelMixin):

    action_name = ADVERSE_EVENT_ACTION_NAME

    description = models.TextField(help_text='Describe the adverse event')

    severity = models.CharField(max_length=20, choices=SEVERITY,
                                help_text='Indicate the severity of the event. In the event of death then select "Death"')

    onset_date = models.DateField(default=timezone.now())

    resolution_date = models.DateField()

    action_taken = models.TextField()

    outcome = models.TextField()

    comment = models.TextField()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = "Subject Adverse Event"
        verbose_name_plural = "Subject Adverse Events"
