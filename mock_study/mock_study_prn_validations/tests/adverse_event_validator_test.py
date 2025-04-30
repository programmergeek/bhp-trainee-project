from django.test import TestCase
from datetime import datetime
from django.core.exceptions import ValidationError
from ..form_validators.adverse_event_validator import AdverseEventValidator


class AdverseEventValidatorTest(TestCase):

    def test_resolution_date(self):

        options = {
            'resolution_date': datetime(2023, 4, 4).date()
        }

        form_validator = AdverseEventValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)

    def test_onset_date(self):

        options = {
            'onset_date': datetime(2045, 1, 1).date()
        }

        form_validator = AdverseEventValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
