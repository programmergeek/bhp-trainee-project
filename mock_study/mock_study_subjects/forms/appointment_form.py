from django import forms
from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.appointment_validator import AppointmentFormValidator
from ..models.appointment import Appointment


class AppointmentForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = AppointmentFormValidator

    class Meta:
        model = Appointment
        fields = '__all__'
