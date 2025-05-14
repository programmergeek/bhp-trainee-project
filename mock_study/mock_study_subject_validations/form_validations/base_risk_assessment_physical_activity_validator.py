from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class BaseRiskAssessmentPhysicalActivityValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='exercise',
            field_required='days_per_week'
        )

        self.not_required_if(
            NO,
            field='exercise',
            field_required='days_per_week'
        )
