from edc_dashboard import UrlConfig
from .patterns import subject_identifier, screening_identifier
from .views.screening.listboard_view import ScreeningListboardView
from .views.subject.listboard.listboard_view import SubjectListboardView

app_name = "mock_study_dashboard"

subject_listboard_url_config = UrlConfig(
    url_name='subject_listboard_url',
    view_class=SubjectListboardView,
    label='subject_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)

screening_listboard_url_config = UrlConfig(
    url_name='screening_listboard_url',
    view_class=ScreeningListboardView,
    label='screening_listboard',
    identifier_label='screening_identifier',
    identifier_pattern=screening_identifier)

urlpatterns = []
urlpatterns += subject_listboard_url_config.listboard_urls
urlpatterns += screening_listboard_url_config.listboard_urls
