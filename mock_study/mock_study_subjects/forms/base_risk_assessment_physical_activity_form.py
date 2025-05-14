from django import forms

from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.base_risk_assessment_physical_activity_validator import BaseRiskAssessmentPhysicalActivityValidator

from ..models.base_risk_assessment_physical_activity import BaseRiskAssessmentPhysicalActivity

class BaseRiskAssessmentPhysicalActivityForm(FormValidatorMixin ,forms.ModelForm):

    form_validator_cls = BaseRiskAssessmentPhysicalActivityValidator

    class Meta:
        model = BaseRiskAssessmentPhysicalActivity
        fields = '__all__'
