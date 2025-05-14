from django import forms

from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.base_risk_assessment_alcohol_validator import BaseRiskAssessmentAlcoholValidator

from ..models.base_risk_assessment_alcohol import BaseRiskAssessmentAlcohol


class BaseRiskAssessmentAlcoholForm(FormValidatorMixin ,forms.ModelForm):

    form_validator_cls = BaseRiskAssessmentAlcoholValidator

    class Meta:
        model = BaseRiskAssessmentAlcohol
        fields = '__all__'
