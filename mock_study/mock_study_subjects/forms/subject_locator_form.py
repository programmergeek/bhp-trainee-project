from django import forms
from ..models.subject_locator import SubjectLocator
from edc_form_validators import FormValidatorMixin
from mock_study_subject_validations.form_validations.subject_locator_validator import SubjectLocatorFormValidator


class SubjectLocatorForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectLocatorFormValidator

    class Meta:
        model = SubjectLocator
        fields = '__all__'
