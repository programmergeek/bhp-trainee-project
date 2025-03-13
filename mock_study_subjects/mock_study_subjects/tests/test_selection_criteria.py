from django.test import TestCase

from model_bakery import baker


class SubjectScreeningTest(TestCase):

    def setUp(self):
        self.subject_screening_doe = baker.make_recipe(
            'mock_study_subjects.patient_doe')

        self.subject_screening_james = baker.make_recipe(
            'mock_study_subjects.patient_james')

    def test_participant_is_eligible(self):
        self.assertEqual(self.subject_screening_doe.eligible, True)

    def test_participant_is_not_eligible(self):
        self.assertEqual(self.subject_screening_james.eligible, False)
