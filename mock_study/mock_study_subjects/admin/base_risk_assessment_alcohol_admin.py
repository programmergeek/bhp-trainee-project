from django.contrib import admin

from ..admin_site import mock_study_admin
from ..models.base_risk_assessment_alcohol import BaseRiskAssessmentAlcohol
from ..forms.base_risk_assessment_alcohol_form import BaseRiskAssessmentAlcoholForm

@admin.register(BaseRiskAssessmentAlcohol, site=mock_study_admin)
class BaseRiskAssessmentAlcoholAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentAlcoholForm

    fieldsets = ((None, {
        'fields':
        [
            'consumes_alcohol',
            'drinks_per_week',
            'amount_of_drinks',
            'report_datetime',
        ] 
    }),)
