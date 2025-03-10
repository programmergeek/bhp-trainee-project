from django.contrib import admin
from ..admin_site import mock_study_admin
from ..fieldsets import other_indirect_contacts_fieldset, indirect_contacts_fieldset
from ..fieldsets import subject_contacts_fieldset
from ..forms.subject_locator_form import SubjectLocatorForm
from ..models.subject_locator import SubjectLocator

from ..fieldsets import work_contacts_fieldset


# class ModelAdminMixin:
#
#     list_per_page = 10
#     date_hierarchy = 'modified'
#     empty_value_display = '-'
#     subject_dashboard_url = 'subject_dashboard_url'
#
#     post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
#         subject_dashboard_url)
#
#     def post_url_on_delete_kwargs(self, request, obj):
#         return dict(subject_identifier=obj.subject_identifier)
#
#     def redirect_url(self, request, obj, post_url_continue=None):
#         if obj:
#             return reverse(settings.DASHBOARD_URL_NAMES.get(
#                 self.subject_dashboard_url),
#                 kwargs=dict(subject_identifier=obj.subject_identifier))
#         else:
#             return super().redirect_url(request, obj, post_url_continue)
#

@admin.register(SubjectLocator, site=mock_study_admin)
class SubjectLocatorAdmin(admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'date_signed',
                'local_clinic',
                'home_village',
            )}),
        subject_contacts_fieldset,
        work_contacts_fieldset,
        indirect_contacts_fieldset,
        other_indirect_contacts_fieldset,
    )

    radio_fields = {
        'may_visit_home': admin.VERTICAL,
        'may_call': admin.VERTICAL,
        'may_sms': admin.VERTICAL,
        'may_call_work': admin.VERTICAL,
        'may_contact_indirectly': admin.VERTICAL}

    list_filter = (
        'may_visit_home',
        'may_call',
        'may_sms',
        'may_call_work',
        'may_contact_indirectly')

    list_display = (
        'subject_identifier',
        'dashboard',
        'visit_home',
        'call',
        'sms',
        'call_work',
        'contact_indirectly')

    search_fields = ('subject_identifier', )
