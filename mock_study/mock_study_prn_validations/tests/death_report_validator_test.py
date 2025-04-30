from django.test import TestCase
from edc_constants.constants import YES
from django.core.exceptions import ValidationError
from ..form_validators.death_report_validator import DeathReportValidator


class DeathReportValidatorTest(TestCase):

    def test_hospital_name(self):

        options = {
            'was_hospitalised': YES
        }

        form_validator = DeathReportValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('hospital_hospitalised', form_validator._errors)

    def test_reason_hospitalised(self):

        options = {
            'was_hospitalised': YES,
            'hospital_hospitalised': 'marina'
        }

        form_validator = DeathReportValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_hospitalised', form_validator._errors)
