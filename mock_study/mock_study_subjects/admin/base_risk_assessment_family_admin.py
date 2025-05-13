from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.base_risk_assessment_family_form import BaseRiskAssessmentFamilyForm
from ..models.base_risk_assessment_family import BaseRiskAssessmentFamily

@admin.register(BaseRiskAssessmentFamily, site=mock_study_admin)
class BaseRiskAssessmentFamilyAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentFamilyForm

    fieldsets = ((None, {
        'fields': [
            'direct_family',
            'extended_family',
            'report_datetime',
        ]
    }),)
