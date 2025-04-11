from django.conf import settings
from edc_model_wrapper import ModelWrapper
from .model_wrapper_mixins.subject_screening_wrapper_mixin import SubjectScreeningModelWrapperMixin


class SubjectScreeningModelWrapper(ModelWrapper, SubjectScreeningModelWrapperMixin):

    model = 'mock_study_subjects.subjectscreening'
    next_url_name = 'screening_identifier'
    next_url_attrs = settings.DASHBOARD_URL_NAMES.get(
        'screening_listboard_url')
