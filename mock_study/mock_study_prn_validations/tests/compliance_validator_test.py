from django.test import TestCase
from ..form_validators.compliance_validator import ComplianceValidator
from django.core.exceptions import ValidationError


class ComplianceValidatorTest(TestCase):

    def test_missed_dosage_reason(self):

        options = {
            'doses_prescribed': 10,
            'doses_taken': 5
        }

        form_validator = ComplianceValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('missed_dosses_reason', form_validator._errors)
