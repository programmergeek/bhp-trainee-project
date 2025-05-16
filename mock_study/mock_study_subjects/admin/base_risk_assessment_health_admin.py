from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.base_risk_assessment_health_form import BaseRiskAssessmentHealthForm
from ..models.base_risk_assessment_health import BaseRiskAssessmentHealth

@admin.register(BaseRiskAssessmentHealth, site=mock_study_admin)
class BaseRiskAssessmentHealthAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentHealthForm

    fieldsets = ((None, {
        'fields': [
           'preexisting_condition_name',
            'preexisting_condition_symptom',
            'preexisting_condition_treatment',
            'preexisting_condition_treatment_side_effects',
            'report_datetime',
        ]
    }),)
