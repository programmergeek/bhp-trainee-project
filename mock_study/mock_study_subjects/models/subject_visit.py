from django.db import models
from ..choices import VISIT_INFO_SOURCE, VISIT_UNSCHEDULED_REASON, VISIT_REASON
from ..constants import NOT_APPLICABLE

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager as BaseCurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin


class CurrentSiteManager(VisitModelManager, BaseCurrentSiteManager):
    # This manager just combines the functions of the VisitModelManager and CurrentSiteManager from their respective edc modules
    pass


class SubjectVisit(
        VisitModelMixin,
        RequiresConsentFieldsModelMixin,
        SiteModelMixin,
        BaseUuidModel):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """
    appointment = models.CharField(max_length=10)

    reason = models.CharField(
        verbose_name='What is the reason for this visit report?',
        max_length=25,
        choices=VISIT_REASON)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        max_length=50,
        choices=VISIT_UNSCHEDULED_REASON,
        default=NOT_APPLICABLE)

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=40,
        choices=VISIT_INFO_SOURCE)

    history = HistoricalRecords()

    objects = VisitModelManager()

    on_site = CurrentSiteManager()

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Mock Study Subject Visit'
        verbose_name_plural = 'Mock Study Subject Visit'
        pass
