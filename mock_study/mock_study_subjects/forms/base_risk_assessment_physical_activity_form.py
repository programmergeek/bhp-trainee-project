from django import forms

from ..models.base_risk_assessment_physical_activity import BaseRiskAssessmentPhysicalActivity

class BaseRiskAssessmentPhysicalActivityForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentPhysicalActivity
        fields = '__all__'
