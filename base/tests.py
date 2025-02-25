import datetime

from django.test import TestCase
from django.utils import timezone

from .models.blood_samples_models import BloodSample
from .models.vitals_model import ParticipantVital


class BloodSampleModelTest(TestCase):

    # Test if you can give the collection date of blood sample to some date in the future.
    def test_future_blood_sample_collection_date(self):

        date = timezone.now() + datetime.timedelta(days=30)
        future_sample = BloodSample(collection_date=date)
        self.assertIs(future_sample.collection_date.date()
                      > timezone.now().date(), False)

    # Test if you can backdate a blood sample collection
    def test_past_blood_sample_collection_date(self):

        date = (timezone.now() + datetime.timedelta(days=-30)).date()
        past_sample = BloodSample(collection_date=date)
        self.assertIs(past_sample.collection_date <
                      timezone.now().date(), False)


class VitalsModelTest(TestCase):

    # participant weghts cannot be less than 0
    def test_negative_weight(self):

        test_weight = -234.0
        test_vital = ParticipantVital(weight=test_weight)
        self.assertIs(test_vital.weight < 0, False)
