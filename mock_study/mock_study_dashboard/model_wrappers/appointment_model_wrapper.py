from edc_subject_dashboard import AppointmentModelWrapper
from .subject_visit_model_wrapper import SubjectVisitModelWrapper


class SubjectAppointmentWrapper(AppointmentModelWrapper):

    visit_model_wrapper_cls = SubjectVisitModelWrapper
