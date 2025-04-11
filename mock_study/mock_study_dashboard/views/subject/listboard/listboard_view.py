from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin
from edc_dashboard.views import ListboardView


from mock_study_dashboard.model_wrappers.subject_consent_model_wrapper import SubjectConsentModelWrapper
from .filters import SubjectListBoardFilters


class SubjectListboardView(EdcBaseViewMixin, ListboardFilterViewMixin, ListboardView):

    listboard_template = 'subject_listboard_template'
    listboard_url = 'screening_listboard_url'

    listboard_view_filters = SubjectListBoardFilters()
    model = 'mock_study_subjects.subjectconsent'
    model_wrapper_cls = SubjectConsentModelWrapper

    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            subject_consent_add_url=self.model_cls().get_absolute_url(),
        )
        return context

    # def get_queryset_filter_options(self, request, *args, **kwargs):
    #     options = super().get_queryset_filter_options(request, *args, **kwargs)
    #     try:
    #         options.pop('site')
    #     except KeyError:
    #         pass
    #     if kwargs.get('subject_identifier'):
    #         options.update(
    #             {'subject_identifier': kwargs.get('subject_identifier')})
    #     return options
