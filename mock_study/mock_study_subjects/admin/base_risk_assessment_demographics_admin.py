from django.contrib import admin

from ..forms.base_risk_assessment_demographics_form import BaseRiskAssessmentDemographicsForms
from ..models.base_risk_assessment_demographics import BaseRiskAssessmentDemographics
from ..admin_site import mock_study_admin

@admin.register(BaseRiskAssessmentDemographics, site=mock_study_admin)
class BaseRiskAssessmentDemographicsAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentDemographicsForms

    fieldsets = ((None, {
        'fields': [
            'marital_status',
            'marital_status_other',
            'race',
            'race_other',
            'employed',
            'education',
            'education_other',
            'report_datetime',
        ]
    }),)
