from django.test import TestCase
from django.core.exceptions import ValidationError
from edc_constants.constants import MALE, YES
from ..form_validations.subject_screening_validator import SubjectScreeningValidator


class ScreeningValidatorTest(TestCase):

    def test_male_pregnant_validator(self):
        options = {
            'gender': MALE,
            'is_pregnant': YES
        }

        form_validator = SubjectScreeningValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('is_pregnant', form_validator._errors)

    def test_male_breastfeeding_validator(self):
        options = {
            'gender': MALE,
            'is_breastfeeding': YES
        }

        form_validator = SubjectScreeningValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('is_breastfeeding', form_validator._errors)
