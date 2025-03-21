from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'mock_study_subject_validations'
    verbose_name = 'Mock Study Subject Validations'
    admin_site_name = 'mock_study_subject_validations_admin'
    pass
