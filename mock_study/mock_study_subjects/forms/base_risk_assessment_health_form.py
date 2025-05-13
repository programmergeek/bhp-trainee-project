from django import forms

from ..models.base_risk_assessment_health import BaseRiskAssessmentHealth

class BaseRiskAssessmentHealthForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentHealth
        fields = '__all__'
