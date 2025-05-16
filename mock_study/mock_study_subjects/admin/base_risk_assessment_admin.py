from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.base_risk_assessment_form import BaseRiskAssessmentForm
from ..models.base_risk_assessment import BaseRiskAssessment

@admin.register(BaseRiskAssessment, site=mock_study_admin)
class BaseRiskAssessmentAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentForm

    fieldsets = ((None, {
        'fields': [
            'drinks_alcohol',
            'drinks_caffeine',
            'preexisting_condition'
        ]
    }),)
