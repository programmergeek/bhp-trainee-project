from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO

from ..form_validations.base_risk_assessment_health_validator import BaseRiskAssessmentHealthValidator

class BaseRiskAssessmentHealthValidatorTest(TestCase):

    def test_reason_for_medication_required(self):
        options = {
            'medication': YES,
            'reason_for_medication': None
        }

        form_validator = BaseRiskAssessmentHealthValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_for_medication', form_validator._errors)
        pass

    def test_side_effects_required(self):
        options = {
            'medication': YES,
            'reason_for_medication': 'afwefawef',
            'side_effects': None
        }

        form_validator = BaseRiskAssessmentHealthValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('side_effects', form_validator._errors)
        pass

    def test_reason_for_medication_not_required(self):
        options = {
            'medication': NO,
            'reason_for_medication': 'aweveavasdfasdf sdfaew ae'
        }

        form_validator = BaseRiskAssessmentHealthValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('reason_for_medication', form_validator._errors)
        pass

    def test_side_effects_not_required(self):
        options = {
            'medication': NO,
            'side_effects': 'afw awef awfawfa'
        }

        form_validator = BaseRiskAssessmentHealthValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('side_effects', form_validator._errors)
        pass
