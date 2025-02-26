from django.db import models


class ParticipantMedicalHistory(models.Model):

    participant_identifier = models.CharField(max_length=50)


class Allergy(models.Model):

    participant_identifier = models.ForeignKey(
        ParticipantMedicalHistory,
        on_delete=models.CASCADE
    )
    allergen = models.CharField(max_length=200)
    reaction = models.TextField()


class Doctor(models.Model):

    name = models.CharField(max_length=200)  # name of the doctor


class Medication(models.Model):

    name = models.CharField(max_length=100)  # name of the medication
    participant_identifier = models.ForeignKey(
        ParticipantMedicalHistory,
        on_delete=models.CASCADE
    )
    prescribed_by = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)


class PreviousMedicalEvents(models.Model):

    date = models.DateField()
    # name of the medical event, e.g stroke
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    hospital = models.CharField(max_length=200)
    participant_identifier = models.ForeignKey(
        ParticipantMedicalHistory,
        on_delete=models.CASCADE
    )
