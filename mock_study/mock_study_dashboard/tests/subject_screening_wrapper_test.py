from django.test import TestCase
from edc_model_wrapper.tests import ModelWrapperTestHelper
from ..model_wrappers.subject_screening_model_wrapper import SubjectScreeningModelWrapper


class TestScreeningModelWrapper(TestCase):

    def test_screening_wrapper(self):
        helper = ModelWrapperTestHelper(
            model_wrapper=SubjectScreeningModelWrapper,
            app_label='mock_study_dashboard',
            screening_identifier='ASDFAGE'
        )

        helper.test(self)
