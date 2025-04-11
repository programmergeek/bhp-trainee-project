from django.conf import settings
from edc_model_wrapper import ModelWrapper
from .model_wrapper_mixins.subject_screening_wrapper_mixin import SubjectScreeningModelWrapperMixin
from .model_wrapper_mixins.subject_consent_model_wrapper_mixin import SubjectConsentModelWrapperMixin
from .subject_screening_model_wrapper import SubjectScreeningModelWrapper


class SubjectConsentModelWrapper(ModelWrapper, SubjectConsentModelWrapperMixin, SubjectScreeningModelWrapperMixin):

    model = 'mock_study_subjects.subjectconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'subject_listboard_url')
    next_url_attrs = ['subject_identifier']

    def subject_screening(self):
        model_obj = self.subject_screening_model_obj or self.subject_screening_cls(
            **self.subject_screening_options)
        return SubjectScreeningModelWrapper(model_obj=model_obj)
