from django import forms

from ..models.base_risk_assessment_family import BaseRiskAssessmentFamily

class BaseRiskAssessmentFamilyForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentFamily
        fields = '__all__'
