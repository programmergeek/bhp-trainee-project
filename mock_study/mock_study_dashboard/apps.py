from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'mock_study_dashbord'
    admin_site_name = 'mock_study_subject_admin'
