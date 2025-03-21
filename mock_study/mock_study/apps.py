from django.apps import AppConfig as DjangoAppConfig
from edc_locator.apps import AppConfig as BaseEdcLocatorAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_appointment.constants import COMPLETE_APPT


class AppConfig(DjangoAppConfig):
    name = 'mock_study'


class EdcLocatorAppConfig(BaseEdcLocatorAppConfig):
    name = 'edc_locator'
    reference_model = 'mock_study_subjects.subjectlocator'


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
