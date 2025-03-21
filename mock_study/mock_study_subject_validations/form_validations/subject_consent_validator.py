from edc_form_validators import FormValidator
from edc_constants.constants import OTHER


class SubjectConsentValidator(FormValidator):

    def clean(self):
        self.required_if(
            OTHER,
            field_required='other_idenity_type',
            field='identity_type'
        )
