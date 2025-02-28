import datetime

from django.test import TestCase
from django.utils import timezone

from .models.blood_samples_models import BloodSample
from .models.vitals_model import ParticipantVital
from .models.participant_medical_history_model import PreviousMedicalEvents, Medication, Doctor, Allergy, ParticipantMedicalHistory


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

    def test_weight_upper_limit(self):

        test_weight = 9000
        test_vital = ParticipantVital(weight=test_weight)
        self.assertIs(test_vital.weight > 500.0, False)


class MedicalHistoryTest(TestCase):

    # can you create a participant's medical history record
    def test_medical_history_creation(self):
        # create main medical history object
        participant_medical_history = ParticipantMedicalHistory.objects.create(
            participant_identifier='12345')

        self.assertEqual(
            participant_medical_history.participant_identifier, "12345")
        self.assertEqual(ParticipantMedicalHistory.objects.count(), 1)

    def test_create_doctor(self):

        doctor = Doctor.objects.create(name='M. Samson')

        self.assertIs(doctor.name, 'M. Samson')

    def test_participant_medication_creation(self):

        participant = ParticipantMedicalHistory.objects.create(
            participant_identifier='P12345'
        )

        doctor = Doctor.objects.create(
            name='M. Samson'
        )

        medication = Medication.objects.create(
            participant_identifier=participant,
            name='test drug',
            prescribed_by=doctor
        )

        self.assertEqual(medication.name, 'test drug')
        self.assertIs(medication.prescribed_by.name, doctor.name)

    def test_create_participant_medical_event(self):

        participant = ParticipantMedicalHistory.objects.create(
            participant_identifier='12345')
        doctor = Doctor.objects.create(name='M. Samson')

        medical_event = PreviousMedicalEvents.objects.create(
            name='Allergic reaction',
            participant_identifier=participant,
            description='Participant was exposed to peanuts during a meal, possibly from cross contamination, and suffered an acute alergic reaction.',
            location='Gaborone',
            hospital='Princess Marina Hospital',
            doctor=doctor,
            date=timezone.now().date()
        )

        self.assertIs(medical_event.name, 'Allergic reaction')

    def test_create_multiple_medical_events(self):

        participant = ParticipantMedicalHistory.objects.create(
            participant_identifier='12345')

        doctor = Doctor.objects.create(name='M. Samson')

        events = []

        for i in range(5):

            events.append(
                PreviousMedicalEvents.objects.create(
                    participant_identifier=participant,
                    doctor=doctor,
                    description='testing '+str(i),
                    name=''+str(i),
                    date=timezone.now(),
                    hospital='Test hospital',
                    location='Gaborone'
                ))

        self.assertEqual(PreviousMedicalEvents.objects.filter(
            participant_identifier=participant).count(), 5)
        pass

    def test_create_allergy(self):

        participant = ParticipantMedicalHistory.objects.create(
            participant_identifier='12345')

        allergy = Allergy.objects.create(
            participant_identifier=participant,
            reaction='test',
            allergen='nuts'
        )

        self.assertIs(allergy.allergen, 'nuts')

    def test_create_multiple_allergies(self):

        participant = ParticipantMedicalHistory.objects.create(
            participant_identifier='12345')

        allergies = []

        for i in range(5):

            allergies.append(Allergy.objects.create(
                participant_identifier=participant,
                allergen=str(i),
                reaction=str(i)
            ))

        self.assertEqual(Allergy.objects.filter(
            participant_identifier=participant).count(), 5)

    # medical events cannot happen in the future

    def test_medical_event_future_dating(self):

        future_date = timezone.now() + datetime.timedelta(days=30)
        medical_event = PreviousMedicalEvents(date=future_date)
        self.assertIs(timezone.now() < medical_event.date, False)

    pass
