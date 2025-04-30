from django.apps import apps
from django.forms import ValidationError
from edc_form_validators import FormValidator


class ComplianceValidator(FormValidator):

    def clean(self):
        self.required_if_true(
            condition=self.cleaned_data.get('doses_taken') < self.cleaned_data.get(
                'doses_prescribed'),
            field_required='missed_dosses_reason')
        self.report_datetime_validator()
        pass

    def report_datetime_validator(self):

        protocol = apps.get_app_config('edc_protocol')
        open_datetime = protocol.study_open_datetime
        close_datetime = protocol.study_close_datetime

        dt_open = open_datetime.replace(tzinfo=None)
        dt_close = close_datetime.replace(tzinfo=None)

        report_datetime = self.cleaned_data.get(
            'report_datetime').replace(tzinfo=None)

        if (report_datetime):
            if (dt_open > report_datetime or dt_close < report_datetime):
                message = {
                    'report_datetime': "Report datetime cannot be before the study open date or after the study close date."
                }
                self._errors.update(message)
                raise ValidationError(message)

        pass
