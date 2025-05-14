from django import forms

from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.base_risk_assessment_caffeine_validator import BaseRiskAssessmentCaffeineValidator

from ..models.base_risk_assessment_caffeine import BaseRiskAssessmentCaffeine

class BaseRiskAssessmentCaffeineForm( FormValidatorMixin, forms.ModelForm):

    form_validator_cls = BaseRiskAssessmentCaffeineValidator

    class Meta:
        model=BaseRiskAssessmentCaffeine
        fields = '__all__'

