from django import forms

from edc_form_validators import FormValidatorMixin

from ..models.base_risk_assessment_caffeine import BaseRiskAssessmentCaffeine

class BaseRiskAssessmentCaffeineForm( FormValidatorMixin, forms.ModelForm):

    class Meta:
        model=BaseRiskAssessmentCaffeine
        fields = '__all__'

