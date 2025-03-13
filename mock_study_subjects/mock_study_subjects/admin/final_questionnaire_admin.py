from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.final_questionnaire_form import FinalQuestionnaireForm
from ..models.final_questionnaire import FinalQuestionnaire


@admin.register(FinalQuestionnaire, site=mock_study_admin)
class FinalQuestionnaireAdmin(admin.ModelAdmin):

    form = FinalQuestionnaireForm

    fieldsets = ((None, {
        'fields': [
            'subject_identifier',
            'participant_experience_with_the_study',
            'percieved_benefits',
            'percieved_challenges',
            'willingness_to_participate_in_future_studies'
        ]
    }),)
