from django.apps import apps
from django.forms import ValidationError
from edc_form_validators import FormValidator
from edc_constants.constants import YES


class DeathReportValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='was_hospitalised',
            field_required='hospital_hospitalised'
        )
        self.required_if(
            YES,
            field='was_hospitalised',
            field_required='reason_hospitalised'
        )
        self.required_if(
            YES,
            field='was_hospitalised',
            field_required='days_hospitalised'
        )
        self.death_date_validator()

    def death_date_validator(self):

        protocol = apps.get_app_config('edc_protocol')
        open_datetime = protocol.study_open_datetime
        close_datetime = protocol.study_close_datetime

        dt_open = open_datetime.replace(tzinfo=None).date()
        dt_close = close_datetime.replace(tzinfo=None).date()

        death_date = self.cleaned_data.get('date_of_death')

        if (death_date):
            if (dt_open > death_date or dt_close < death_date):
                message = {
                    'date_of_death': "Date of death cannot be before the study open date or after the study close date."
                }
                self._errors.update(message)
                raise ValidationError(message)

        pass
