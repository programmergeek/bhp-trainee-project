from django import forms

from edc_form_validators import FormValidatorMixin

from ..models.base_risk_assessment_alcohol import BaseRiskAssessmentAlcohol


class BaseRiskAssessmentAlcoholForm(FormValidatorMixin ,forms.ModelForm):

    class Meta:
        model = BaseRiskAssessmentAlcohol
        fields = '__all__'
