from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = "Mock Study Subject"
    site_header = "Mock Study Subject"
    index_title = "Mock Study Subject"
    site_url = "/mock_study_subject/list/"


mock_study_admin = AdminSite(name='mock_study_subject_admin')
