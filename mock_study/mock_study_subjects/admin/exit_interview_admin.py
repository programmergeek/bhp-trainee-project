from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.exit_interview_form import ExitInterviewForm
from ..models.exit_interview import ExitInterview


@admin.register(ExitInterview, site=mock_study_admin)
class ExitInterviewAdmin(admin.ModelAdmin):

    form = ExitInterviewForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'summary',
            'investigator_observation',
            'final_comments',
            'final_recommendation'
        ]
    }),)
