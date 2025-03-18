from django.apps import AppConfig as DjangoApponfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_appointment.constants import COMPLETE_APPT


class AppConfig(DjangoApponfig):
    name = 'mock_study_subjects'
    verbose_name = 'Mock Study Subject CRFs'
    admin_site_name = 'mock_study_subject_admin'


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='cancer_subject.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='cancer_subject.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT)
        ])
