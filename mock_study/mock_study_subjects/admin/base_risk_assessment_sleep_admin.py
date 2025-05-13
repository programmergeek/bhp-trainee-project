from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.base_risk_assessment_sleep_form import BaseRiskAssessmentSleepForm
from ..models.base_risk_assessment_sleep import BaseRiskAssessmentSleep

@admin.register(BaseRiskAssessmentSleep, site=mock_study_admin)
class BaseRiskAssessmentSleepAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentSleepForm

    fieldsets = ((None, {
        'fields': [
            'sleep',
            'restlessness',
            'night_shift',
            'hours_slept',
            'report_datetime',
        ]
    }),)
