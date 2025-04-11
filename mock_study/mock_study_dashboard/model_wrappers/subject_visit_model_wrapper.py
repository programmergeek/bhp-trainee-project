from django.conf import settings
from edc_subject_dashboard import SubjectVisitModelWrapper


class SubjectVisitModelWrapper(SubjectVisitModelWrapper):
    model = 'mock_study_subjects.subjectvisit'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'mock_study_subject_listboard_url')
    next_url_attrs = ['subject_identifier']
