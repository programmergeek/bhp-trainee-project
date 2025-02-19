from django.db import models

class PaticipantVitals(models.Model):

    participant_identifier = models.CharField(max_length=50)
    height = models.FloatField()
    blood_pressure = models.CharField(max_length=50)
    weight = models.FloatField()
