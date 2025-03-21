from django import forms
from edc_form_validators import FormValidator
from edc_constants.constants import MALE, YES


class SubjectScreeningValidator(FormValidator):

    def clean(self):
        super().clean()
        self.clean_male_pregnant_breastfeeding()

    def clean_male_pregnant_breastfeeding(self):

        data = self.cleaned_data
        gender = data.get('gender')
        is_pregnant = data.get('is_pregnant')
        is_breastfeeding = data.get('is_breastfeeding')

        if (is_breastfeeding == YES and is_pregnant == YES and gender == MALE):
            raise forms.ValidationError({
                'is_pregnant': 'Male subjects cannot be pregnant.',
                'is_breastfeeding': 'Male subjectes cannot breastfeed.'
            })

        elif (is_pregnant == YES and gender == MALE):
            raise forms.ValidationError({
                'is_pregnant': 'Male subjects cannot be pregnant.'
            })

        elif (is_breastfeeding == YES and gender == MALE):
            raise forms.ValidationError({
                'is_breastfeeding': 'Male subjectes cannot breastfeed.'
            })
