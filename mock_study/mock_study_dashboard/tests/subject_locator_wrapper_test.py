from django.test import TestCase
from edc_model_wrapper.tests import ModelWrapperTestHelper
from ..model_wrappers.subject_locator_model_wrapper import SubjectLocatorWrapper


class TestConsentModelWraper(TestCase):

    def test_consent_wrapper(self):
        helper = ModelWrapperTestHelper(
            model_wrapper=SubjectLocatorWrapper,
            app_label='mock_study_dashboard',
            subject_identifier="999-0923"
        )

        helper.test(self)
