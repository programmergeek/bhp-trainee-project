from edc_appointment.form_validators import AppointmentFormValidator as BaseAppointmentFormValidator


class AppointmentFormValidator(BaseAppointmentFormValidator):

    appointment_model = 'mock_study_subjects.appointment'
