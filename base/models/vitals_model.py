from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ParticipantVital(models.Model):

    participant_identifier = models.CharField(max_length=50)
    height = models.FloatField()
    blood_pressure = models.CharField(max_length=50)
    weight = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    baseline = models.BooleanField(default=True)
