from django import forms
from edc_form_validators import FormValidatorMixin
from mock_study_prn_validations.form_validators.adverse_event_validator import AdverseEventValidator
from ..models.adverse_event_report import AdverseEvent


class AdverseEventForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = AdverseEventValidator

    class Meta:
        model = AdverseEvent
        fields = "__all__"
