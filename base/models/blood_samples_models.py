from django.db import models


class BloodSample(models.Model):

    participant_identifier = models.CharField(max_length=50)
    sample_id = models.CharField(max_length=20)
    collection_date = models.DateTimeField()
    requested_test = models.CharField(max_length=256)
    phlebotomist_signature = models.CharField(max_length=256)
