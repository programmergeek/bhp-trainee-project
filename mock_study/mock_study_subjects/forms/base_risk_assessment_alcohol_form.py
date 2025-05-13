from django import forms

from ..models.base_risk_assessment_alcohol import BaseRiskAssessmentAlcohol

class BaseRiskAssessmentAlcoholForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentAlcohol
        fields = '__all__'
