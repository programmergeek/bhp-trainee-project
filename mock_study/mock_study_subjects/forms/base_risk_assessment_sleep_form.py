from django import forms

from ..models.base_risk_assessment_sleep import BaseRiskAssessmentSleep

class BaseRiskAssessmentSleepForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentSleep
        fields = '__all__'
