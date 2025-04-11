from django import forms
from ..models.subject_locator import SubjectLocator
from edc_form_validators import FormValidatorMixin
from edc_locator.forms.subject_locator_form_validator import SubjectLocatorFormValidator


class SubjectLocatorForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectLocatorFormValidator

    class Meta:
        model = SubjectLocator
        fields = '__all__'
