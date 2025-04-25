from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = "Mock Study PRN"
    site_header = "Mock Study PRN"
    index_title = "Mock Study PRN"
    site_url = "/prn"


mock_study_prn_admin = AdminSite(name='mock_study_prn_admin')
