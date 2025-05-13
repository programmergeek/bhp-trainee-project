from django.contrib import admin

from ..forms.base_risk_assessment_diet_form import BaseRiskAssessmentDietForm
from ..models.base_risk_assessment_diet import BaseRiskAssessmentDiet
from ..admin_site import mock_study_admin


@admin.register(BaseRiskAssessmentDiet, site=mock_study_admin)
class BaseRiskAssessmentDietAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentDietForm

    fieldsets = ((None, {
        'fields': [
            'salty_foods',
            'saturated_fats',
            'red_meats',
            'fruits_and_veg',
            'grain',
            'nuts',
            'low_fat_dairy',
            'report_datetime',
        ]
    }),)
