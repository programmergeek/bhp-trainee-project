from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.base_risk_assessment_health_form import BaseRiskAssessmentHealthForm
from ..models.base_risk_assessment_health import BaseRiskAssessmentHealth

@admin.register(BaseRiskAssessmentHealth, site=mock_study_admin)
class BaseRiskAssessmentHealthAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentHealthForm

    fieldsets = ((None, {
        'fields': [
            'medication',
            'reason_for_medication',
            'side_effects',
            'heart_attack',
            'aneurysm',
            'stroke',
            'kidney_disease',
            'report_datetime',
        ]
    }),)
