from django import forms

from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.base_risk_assessment_demographics_validator import BaseRiskAssessmentDemographicsValidator

from ..models.base_risk_assessment_demographics import BaseRiskAssessmentDemographics

class BaseRiskAssessmentDemographicsForms( FormValidatorMixin, forms.ModelForm):

    form_validator_cls = BaseRiskAssessmentDemographicsValidator

    class Meta:
        model = BaseRiskAssessmentDemographics
        fields = '__all__'
