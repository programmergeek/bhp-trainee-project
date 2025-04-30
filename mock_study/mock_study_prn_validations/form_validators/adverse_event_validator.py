from edc_form_validators import FormValidator
from django.forms import ValidationError
from django.apps import apps


class AdverseEventValidator(FormValidator):

    protocol = apps.get_app_config('edc_protocol')
    open_datetime = protocol.study_open_datetime
    close_datetime = protocol.study_close_datetime

    dt_open = open_datetime.replace(tzinfo=None).date()
    dt_close = close_datetime.replace(tzinfo=None).date()

    def clean(self):
        self.onset_date_validator()
        self.resolution_date_validator()
        pass

    def onset_date_validator(self):
        onset_date = self.cleaned_data.get('onset_date')
        if (onset_date):
            if (self.dt_open > onset_date or self.dt_close < onset_date):
                message = {
                    'onset_date': "Onset date cannot be before the study open date or after the study close date."
                }
                self._errors.update(message)
                raise ValidationError(message)

    def resolution_date_validator(self):

        resolution_date = self.cleaned_data.get('resolution_date')

        if (resolution_date):
            if (self.dt_open > resolution_date or self.dt_close < resolution_date):
                message = {
                    'resolution_date': "Resolution date cannot be before the study open date or after the study close date."
                }
                self._errors.update(message)
                raise ValidationError(message)
