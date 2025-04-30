from django.test import TestCase
from datetime import datetime
from ..form_validators.compliance_validator import ComplianceValidator
from django.core.exceptions import ValidationError


class ComplianceValidatorTest(TestCase):

    def test_missed_dosage_reason(self):

        options = {
            'doses_prescribed': 10,
            'doses_taken': 5,
            'report_datetime': datetime(2004, 5, 2, 23, 0, 0)
        }

        form_validator = ComplianceValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)

    def test_report_datetime(self):

        options = {
            'doses_prescribed': 10,
            'doses_taken': 5,
            'report_datetime': datetime(2004, 5, 2, 23, 0, 0)
        }

        form_validator = ComplianceValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('report_datetime', form_validator._errors)
