from django import forms

from ..models.base_risk_assessment_diet import BaseRiskAssessmentDiet

class BaseRiskAssessmentDietForm(forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentDiet
        fields = '__all__'
