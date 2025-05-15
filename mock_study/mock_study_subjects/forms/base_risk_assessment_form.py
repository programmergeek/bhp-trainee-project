from django import forms

from ..models.base_risk_assessment import BaseRiskAssessment

class BaseRiskAssessmentForm(forms.ModelForm):

    class Meta:
        model=BaseRiskAssessment
        fields='__all__'
