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
