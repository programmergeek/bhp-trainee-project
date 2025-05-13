from django import forms

from ..models.base_risk_assessment_caffeine import BaseRiskAssessmentCaffeine

class BaseRiskAssessmentCaffeineForm(forms.ModelForm):

    class Meta:
        model=BaseRiskAssessmentCaffeine
        fields = '__all__'

