from django.db import models
from ..choices import VISIT_INFO_SOURCE, VISIT_UNSCHEDULED_REASON, VISIT_REASON
from ..constants import NOT_APPLICABLE


class CurrentSiteManager:
    pass


class SubjectVisit:

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

    on_site = CurrentSiteManager()

    class Meta:
        pass
