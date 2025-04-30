from edc_form_validators import FormValidator


class ComplianceValidator(FormValidator):

    def clean(self):
        self.required_if_true(
            condition=self.cleaned_data.get('doses_taken') < self.cleaned_data.get(
                'doses_prescribed'),
            field_required='missed_dosses_reason')
        pass
