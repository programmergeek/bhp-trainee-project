from django import forms
from ..models.subject_vitals import SubjectVitals
from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.subject_vitals_validator import SubjectVitalsValidator


class SubjectVitalsForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectVitalsValidator

    class Meta:
        model = SubjectVitals
        fields = '__all__'
