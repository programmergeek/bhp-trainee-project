from edc_form_validators import FormValidator
from edc_constants.constants import MALE


class SubjectScreeningValidator(FormValidator):

    def clean(self):
        super().clean()
        self.applicable_if_true(
            field='gender',
            condition=self.cleaned_data.get('gender') != MALE,
            field_applicable='is_pregnant'
        )

        self.applicable_if_true(
            field='gender',
            condition=self.cleaned_data.get('gender') != MALE,
            field_applicable='is_breastfeeding'
        )
