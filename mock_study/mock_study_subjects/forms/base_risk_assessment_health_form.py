from django import forms

from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.base_risk_assessment_health_validator import BaseRiskAssessmentHealthValidator

from ..models.base_risk_assessment_health import BaseRiskAssessmentHealth

class BaseRiskAssessmentHealthForm( FormValidatorMixin, forms.ModelForm):

    form_validator_cls = BaseRiskAssessmentHealthValidator

    class Meta:
        model = BaseRiskAssessmentHealth
        fields = '__all__'
