from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'mock_study_prn'
    verbose_name = 'Mock Study PRN'
    admin_site_name = 'mock_study_prn_admin'
