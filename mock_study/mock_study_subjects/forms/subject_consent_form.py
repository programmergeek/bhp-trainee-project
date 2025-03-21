from django import forms
from edc_form_validators.form_validator_mixin import FormValidatorMixin

from ..models.subject_consent import SubjectConsent
from mock_study_subject_validations.form_validations.subject_consent_validator import SubjectConsentValidator


class SubjectConsentForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectConsentValidator

    class Meta:
        model = SubjectConsent
        fields = '__all__'
