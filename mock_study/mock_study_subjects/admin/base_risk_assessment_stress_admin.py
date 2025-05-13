from django.contrib import admin

from ..admin_site import mock_study_admin
from ..models.base_risk_assessment_stress import BaseRiskAssessmentStress
from ..forms.base_risk_assessment_stress_form import BaseRiskAssessmentStressForm

@admin.register(BaseRiskAssessmentStress, site=mock_study_admin)
class BaseRiskAssessmentStressAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentStressForm

    fieldsets = ((None, {
        'fields': [
            'work_stress',
            'home_stress',
            'report_datetime',
        ]
    }),)
