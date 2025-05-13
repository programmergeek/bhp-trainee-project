from django import forms

from ..models.base_risk_assessment_stress import BaseRiskAssessmentStress

class BaseRiskAssessmentStressForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentStress
        fields = '__all__'
