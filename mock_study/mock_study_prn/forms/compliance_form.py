from django import forms
from edc_form_validators import FormValidatorMixin
from mock_study_prn_validations.form_validators.compliance_validator import ComplianceValidator
from ..models.compliance import ComplianceReport


class ComplianceForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = ComplianceValidator

    class Meta:
        model = ComplianceReport
        fields = "__all__"
