from django.contrib import admin
from ..admin_site import mock_study_admin
from ..forms.subject_locator_form import SubjectLocatorForm
from ..models.subject_locator import SubjectLocator
from edc_base.modeladmin_mixins import audit_fieldset_tuple
from ..fieldsets import other_indirect_contacts_fieldset, indirect_contacts_fieldset, subject_contacts_fieldset, work_contacts_fieldset


@admin.register(SubjectLocator, site=mock_study_admin)
class SubjectLocatorAdmin(admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'date_signed',
            )}),
        subject_contacts_fieldset,
        work_contacts_fieldset,
        indirect_contacts_fieldset,
        audit_fieldset_tuple,
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
        'visit_home',
        'call',
        'sms',
        'call_work',
        'contact_indirectly')

    search_fields = ('subject_identifier', )
