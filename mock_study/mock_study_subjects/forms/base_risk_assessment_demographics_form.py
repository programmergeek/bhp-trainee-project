from django import forms

from ..models.base_risk_assessment_demographics import BaseRiskAssessmentDemographics

class BaseRiskAssessmentDemographicsForms(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentDemographics
        fields = '__all__'
