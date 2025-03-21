from django import forms
from edc_form_validators import FormValidatorMixin

from ..models.subject_screening import SubjectScreening
from mock_study_subject_validations.form_validations.subject_screening_validator import SubjectScreeningValidator


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectScreeningValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
