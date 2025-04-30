from datetime import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..form_validators.subject_offstudy_validator import SubjectOffStudyValidator


class SubjectOffStudyValidatorTest(TestCase):

    def test_offstudy_date_before_study(self):
        options = {
            'off_study_date': datetime(2023, 4, 4)
        }

        form_validator = SubjectOffStudyValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)

    def test_offstudy_date_after_study(self):

        options = {
            'off_study_date': datetime(2045, 1, 1)
        }

        form_validator = SubjectOffStudyValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
