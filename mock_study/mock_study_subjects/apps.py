from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'mock_study_subjects'
    verbose_name = 'Mock Study Subject CRFs'
    admin_site_name = 'mock_study_subject_admin'

    screening_age_adult_upper = 99
    screening_age_adult_lower = 18
