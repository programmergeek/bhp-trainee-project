from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO

from ..form_validations.base_risk_assessment_physical_activity_validator import BaseRiskAssessmentPhysicalActivityValidator

class BaseRiskAssessmentPhysicalActivityValidatorTest(TestCase):

    def test_days_per_week_required(self):
        options = {
            'exercise': YES,
            'days_per_week': None
        }

        form_validator = BaseRiskAssessmentPhysicalActivityValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('days_per_week', form_validator._errors)

    def test_days_per_week_not_required(self):
        options = {
            'exercise': NO,
            'days_per_week': 3
        }

        form_validator = BaseRiskAssessmentPhysicalActivityValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('days_per_week', form_validator._errors)
