from django.test import TestCase
from ..form_validators.final_questionnaire_validator import FinalQuestionnaireValidator
from edc_constants.constants import NO
from django.core.exceptions import ValidationError


class FinalQuestionnaireValidatorTest(TestCase):

    def test_study_purpose_comment(self):

        options = {
            'study_purpose': NO,
        }

        form_validator = FinalQuestionnaireValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('study_purpose_grievance', form_validator._errors)

    def test_respectful_staff_comment(self):

        options = {
            'respectful_staff': NO,
        }

        form_validator = FinalQuestionnaireValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('respectful_staff_comment', form_validator._errors)

    def test_instrcution_clearity_comment_disagree(self):

        options = {
            'instruction_clearity': 'disagree',
        }

        form_validator = FinalQuestionnaireValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('instruction_clearity_grievance', form_validator._errors)

    def test_instruction_clearity_comment_strongly_disagree(self):

        options = {
            'instruction_clearity': 'strongly_disagree',
        }

        form_validator = FinalQuestionnaireValidator(cleaned_data=options)

        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('instruction_clearity_grievance', form_validator._errors)
