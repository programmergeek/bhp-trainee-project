from django.contrib import admin
from ..admin_site import mock_study_prn_admin
from ..forms.final_questionnaire_form import FinalQuestionnaireForm
from ..models.final_questionnaire import FinalQuestionnaire


@admin.register(FinalQuestionnaire, site=mock_study_prn_admin)
class FinalQuestionnareAdmin(admin.ModelAdmin):

    form = FinalQuestionnaireForm

    fieldsets = ((None, {
        'fields': (
            'subject_identifier',
            'experience_rating',
            'study_purpose',
            'study_purpose_grievance',
            'respectful_staff',
            'visit',
            'adherence',
            'instruction_clearity',
            'instruction_clearity_grievance',
            'benefits',
            'challenges',
            'paricipate_again'
        )
    }),)
