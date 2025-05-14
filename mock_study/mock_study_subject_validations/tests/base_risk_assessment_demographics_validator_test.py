from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import OTHER

from ..form_validations.base_risk_assessment_demographics_validator import BaseRiskAssessmentDemographicsValidator


class BaseRiskAssessmentDemographicsValidatorTest(TestCase):

    def test_other_marital_status(self):
        options = {
            'marital_status': OTHER,
            'marital_status_other': None
        }

        form_validator = BaseRiskAssessmentDemographicsValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('marital_status_other', form_validator._errors)
        pass

    def test_other_race(self):
        options = {
            'race': OTHER,
            'race_other': None
        }
        form_validator = BaseRiskAssessmentDemographicsValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('race_other', form_validator._errors)
        pass

    def test_other_education(self):
        options = {
            'education': OTHER,
            'education_other': None
        }
        form_validator = BaseRiskAssessmentDemographicsValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('education_other', form_validator._errors)
        pass
