from django.test import TestCase
from django.core.exceptions import ValidationError
from mock_study_subject_validations.form_validations.subject_consent_validator import SubjectConsentValidator
from edc_constants.constants import OTHER


class SubjectConsentValidatorTest(TestCase):

    def test_consent_validator(self):

        options = {
            'other_identity_type': None,
            'identity_type': OTHER
        }

        form_validator = SubjectConsentValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
