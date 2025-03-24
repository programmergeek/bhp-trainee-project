from django.db import models
from edc_appointment.managers import AppointmentManager
from edc_appointment.model_mixins import AppointmentModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseModel
from ..choices import ENROLLMENT_SITES


class Appointment(AppointmentModelMixin, BaseModel):

    subject_identifier = models.CharField(max_length=20)

    datetime = models.DateTimeField()

    site = models.CharField(max_length=30, choices=ENROLLMENT_SITES)

    objects = AppointmentManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,
                self.visit_schedule_name,
                self.schedule_name,
                self.visit_code,
                )

    class Meta(AppointmentModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        pass
