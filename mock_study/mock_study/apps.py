from django.apps import AppConfig as DjangoAppConfig
from dateutil.tz import gettz
from edc_locator.apps import AppConfig as BaseEdcLocatorAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_protocol.apps import AppConfig as EdcProtocolBaseAppConfig
from datetime import datetime


class AppConfig(DjangoAppConfig):
    name = 'mock_study'


class EdcLocatorAppConfig(BaseEdcLocatorAppConfig):
    name = 'edc_locator'
    reference_model = 'mock_study_subjects.subjectlocator'


class EdcProtocolAppConfig(EdcProtocolBaseAppConfig):

    protocol = 'MS942'
    protocol_number = '093'
    protocol_name = 'Mock Study'
    protocol_title = 'Mock Study'
    study_open_datetime = datetime(2025, 8, 1, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2029, 5, 30, 23, 59, 59, tzinfo=gettz('UTC'))


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='mock_study_subjects.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='mock_study_subjects.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT)
        ])
