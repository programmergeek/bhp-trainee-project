from django import forms
from edc_form_validators import FormValidatorMixin
from mock_study_prn_validations.form_validators.death_report_validator import DeathReportValidator
from ..models.death_reports import DeathReport


class DeathReportForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = DeathReportValidator

    class Meta:
        model = DeathReport
        fields = "__all__"
