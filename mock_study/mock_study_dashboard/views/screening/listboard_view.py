from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin
from edc_dashboard.views import ListboardView


from ...model_wrappers.subject_screening_model_wrapper import SubjectScreeningModelWrapper
from .filters import ScreeningListBoardFilters


class ScreeningListboardView(EdcBaseViewMixin, ListboardFilterViewMixin, ListboardView):

    listboard_template = 'screening_listboard_template'
    listboard_url = 'screening_listboard_url'

    listboard_view_filters = ScreeningListBoardFilters()
    model = 'mock_study_subjects.subjectscreening'
    model_wrapper_cls = SubjectScreeningModelWrapper

    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            subject_screening_add_url=self.model_cls().get_absolute_url(),)
        return context
