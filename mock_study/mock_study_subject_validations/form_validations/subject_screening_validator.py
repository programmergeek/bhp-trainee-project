from edc_form_validators import FormValidator
from edc_constants.constants import FEMALE


class SubjectScreeningValidator(FormValidator):

    def clean(self):
        self.applicable_if_true(
            field='gender',
            condition=self.cleaned_data.get('gender') == FEMALE,
            field_applicable='is_pregnant'
        )

        self.applicable_if_true(
            field='gender',
            condition=self.cleaned_data.get('gender') == FEMALE,
            field_applicable='is_breastfeeding'
        )
