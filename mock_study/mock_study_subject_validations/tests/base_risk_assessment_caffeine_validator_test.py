from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO

from ..form_validations.base_risk_assessment_caffeine_validator import BaseRiskAssessmentCaffeineValidator

class BaseRiskAssessmentCaffeineValidatorTest(TestCase):
    
    def test_days_drinking_per_week_required(self):
        options = {
            'consumes_caffeine': YES,
            'drinks_per_week': None,
        }

        form_validator = BaseRiskAssessmentCaffeineValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('drinks_per_week', form_validator._errors)
        pass

    def test_amount_of_drinks_required(self):
        options = {
            'consumes_caffeine': YES,
            'drinks_per_week': 3,
            'amount_of_drinks': None
        }
        form_validator = BaseRiskAssessmentCaffeineValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('amount_of_drinks', form_validator._errors)
        pass

    def test_days_drinking_per_week_not_required(self):
        options = {
            'consumes_caffeine': NO,
            'drinks_per_week': 3,
        }
        form_validator = BaseRiskAssessmentCaffeineValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('drinks_per_week', form_validator._errors)
        pass

    def test_amount_of_drinks_per_week_not_required(self):
        options = {
            'consumes_caffeine': NO,
            'amount_of_drinks': 3
        }
        form_validator = BaseRiskAssessmentCaffeineValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('amount_of_drinks', form_validator._errors)
        pass

    pass
