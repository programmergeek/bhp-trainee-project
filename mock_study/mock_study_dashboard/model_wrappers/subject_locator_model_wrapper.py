from django.conf import settings
from edc_model_wrapper.wrappers import ModelWrapper
from model_wrapper_mixins import SubjectLocatorModelWrapperMixin, SubjectConsentModelWrapperMixin


class SubjectLocatorWrapper(SubjectLocatorModelWrapperMixin, SubjectConsentModelWrapperMixin, ModelWrapper):

    model = 'mock_study_subjects.subjectlocator'
    next_url_attrs = ['subject_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('subject_dashboard_url')
