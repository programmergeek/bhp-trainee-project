from django.contrib import admin

from ..admin_site import mock_study_admin
from ..forms.base_risk_assessment_caffeine_form import BaseRiskAssessmentCaffeineForm
from ..models.base_risk_assessment_caffeine import BaseRiskAssessmentCaffeine


@admin.register(BaseRiskAssessmentCaffeine, site=mock_study_admin)
class BaseRiskAssessmentCaffeineAdmin(admin.ModelAdmin):

    form = BaseRiskAssessmentCaffeineForm

    fieldsets = ((None, {
        'fields': [
            'consumes_caffeine',
            'drinks_per_week',
            'amount_of_drinks',
            'report_datetime',
        ]
    }),)
