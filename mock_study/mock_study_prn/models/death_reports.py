from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseModel
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import
from ..action_items.death_report_action_item import DEATH_REPORT_ACTION_ITEM_NAME
from edc_constants.choices import YES_NO


class DeathReport(SiteModelMixin, ActionModelMixin, BaseModel):

    action_name = DEATH_REPORT_ACTION_ITEM_NAME

    date_of_death = models.DateField()

    cause_of_death = models.TextField()

    is_death_date_estimated = models.CharField(max_length=3, choices=YES_NO)

    source_of_info = models.TextField(
        verbose_name="What is your source of information on the death of the participant?")

    was_hospitalised = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was the participant hospitalised before their death?")

    hospital_hospitalised = models.CharField(
        max_length=200,
        verbose_name="What is the name of the hospital the participant was hospitalised in?")

    reason_hospitalised = models.TextField(
        verbose_name="If they were hospitalised, why?")

    days_hospitalised = models.IntegerField(
        default=0, verbose_name="For how many days were they hospitalised?")

    history = HistoricalRecords()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = "Death Report"
        verbose_name_plural = "Death Reports"
