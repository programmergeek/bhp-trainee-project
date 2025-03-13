from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.adverse_event_form import AdverseEventForm
from ..models.adverse_event import AdverseEvent


@admin.register(AdverseEvent, site=mock_study_admin)
class AdverseEventAdmin(admin.ModelAdmin):

    form = AdverseEventForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'site',
            'description',
            'severity',
            'onset_date',
            'resolution_date',
            'action_taken',
            'outcome',
            'investigator_review',
            'investigator_comment',
            'study_intervention_relationship'
        ]
    }),)
