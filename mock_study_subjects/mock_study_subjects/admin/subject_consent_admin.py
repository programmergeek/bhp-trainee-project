from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
# from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import mock_study_admin
from ..forms.subject_consent_form import SubjectConsentForm
from ..models.subject_consent import SubjectConsent
from ..models.subject_visit import SubjectVisit


# class ModelAdminMixin(ModelAdminRevisionMixin):
#
#     list_per_page = 10
#     date_hierarchy = 'modified'
#     empty_value_display = '-'
#
#     def redirect_url(self, request, obj, post_url_continue=None):
#         redirect_url = super().redirect_url(
#             request, obj, post_url_continue=post_url_continue)
#         if request.GET.dict().get('next'):
#             url_name = request.GET.dict().get('next').split(',')[0]
#             attrs = request.GET.dict().get('next').split(',')[1:]
#             options = {k: request.GET.dict().get(k)
#                        for k in attrs if request.GET.dict().get(k)}
#             options.update(subject_identifier=obj.subject_identifier)
#             try:
#                 redirect_url = reverse(url_name, kwargs=options)
#             except NoReverseMatch as e:
#                 raise Exception(
#                     f'{e}. Got url_name={url_name}, kwargs={options}.')
#         return redirect_url
#

@admin.register(SubjectConsent, site=mock_study_admin)
class SubjectConsentAdmin(admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'gender',)}),
        ('Review Questions', {
            'fields': (),
            'description': 'The following questions are directed to the interviewer.'}),
    )

    search_fields = ('subject_identifier', 'identity')

    readonly_fields = ('screening_identifier',)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))

    def view_on_site(self, obj):
        dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
            'subject_dashboard_url')
        try:
            return reverse(
                dashboard_url_name, kwargs=dict(
                    subject_identifier=obj.subject_identifier))
        except NoReverseMatch:
            return super().view_on_site(obj)

    def delete_view(self, request, object_id, extra_context=None):
        """Prevent deletion if SubjectVisit objects exist.
        """
        extra_context = extra_context or {}
        obj = SubjectConsent.objects.get(id=object_id)
        try:
            protected = [SubjectVisit.objects.get(
                subject_identifier=obj.subject_identifier)]
        except ObjectDoesNotExist:
            protected = None
        except MultipleObjectsReturned:
            protected = SubjectVisit.objects.filter(
                subject_identifier=obj.subject_identifier)
        extra_context.update({'protected': protected})
        return super().delete_view(request, object_id, extra_context)
