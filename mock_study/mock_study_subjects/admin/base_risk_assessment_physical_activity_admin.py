from django.contrib import admin

from ..admin_site import mock_study_admin
from ..models.base_risk_assessment_physical_activity import BaseRiskAssessmentPhysicalActivity
from ..forms.base_risk_assessment_physical_activity_form import BaseRiskAssessmentPhysicalActivityForm

@admin.register(BaseRiskAssessmentPhysicalActivity, site=mock_study_admin)
class BaseRiskAssessmentPhysicalActivityAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentPhysicalActivityForm

    fieldsets = ((None, {
        'fields': [
            'exercise',
            'days_per_week',
            'report_datetime',
        ]
    }),)
