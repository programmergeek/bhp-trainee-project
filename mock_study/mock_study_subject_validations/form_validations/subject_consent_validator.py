from edc_form_validators import FormValidator


class SubjectConsentValidator(FormValidator):

    def clean(self):
        self.validate_other_specify(
            other_specify_field='other_idenity_type',
            field='identity_type'
        )
