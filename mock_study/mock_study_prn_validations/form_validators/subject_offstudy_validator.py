from edc_form_validators import FormValidator
from django.forms import ValidationError
from django.apps import apps


class SubjectOffStudyValidator(FormValidator):

    def clean(self):
        self.report_datetime_validator()
        self.test_offstudy_date_validator()
        pass

    def test_offstudy_date_validator(self):
        # validate that the off study date is between the open and close dates of the study.
        protocol = apps.get_app_config('edc_protocol')
        open_datetime = protocol.study_open_datetime
        close_datetime = protocol.study_close_datetime

        offstudy_date = self.cleaned_data.get('off_study_date')

        dt_open = open_datetime.replace(tzinfo=None).date()
        dt_close = close_datetime.replace(tzinfo=None).date()

        if (dt_open > offstudy_date or dt_close < offstudy_date):
            message = {
                'off_study_date': "Off study date cannot be before or after the open and close date of the study"
            }
            self._errors.update(message)
            raise ValidationError(message)

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
