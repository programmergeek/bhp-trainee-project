from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class BaseRiskAssessmentHealthValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='medication',
            field_required='reason_for_medication'
        )

        self.required_if(
            YES,
            field='medication',
            field_required='side_effects'
        )

        self.not_required_if(
            NO,
            field='medication',
            field_required='reason_for_medication'
        )

        self.not_required_if(
            NO,
            field='medication',
            field_required='side_effects'
        )
