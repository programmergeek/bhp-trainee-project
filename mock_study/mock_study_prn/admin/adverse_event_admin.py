from django.contrib import admin
from ..admin_site import mock_study_prn_admin
from ..forms.adverse_event_form import AdverseEventForm
from ..models.adverse_event_report import AdverseEvent


@admin.register(AdverseEvent, site=mock_study_prn_admin)
class AdverseEventAdmin(admin.ModelAdmin):

    form = AdverseEventForm

    fieldsets = ((None, {
        'fields': (
            'subject_identifier',
            'description',
            'severity',
            'onset_date',
            'resolution_date',
            'action_taken',
            'outcome',
            'comment'
        )
    }),)
