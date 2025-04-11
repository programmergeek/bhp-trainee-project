from django.test import TestCase
from edc_model_wrapper.tests import ModelWrapperTestHelper
from ..model_wrappers.subject_consent_model_wrapper import SubjectConsentModelWrapper


class TestConsentModelWraper(TestCase):

    def test_consent_wrapper(self):
        helper = ModelWrapperTestHelper(
            model_wrapper=SubjectConsentModelWrapper,
            app_label='mock_study_dashboard',
            screening_identifier='ASDFAGE',
            subject_identifier="999-0923"
        )

        helper.test(self)
