from django.db import models


class ComplianceForm(models.Model):

    participant_identifier = models.CharField(max_length=50)
    dose_taken = models.CharField(max_length=100)
    dose_prescribed = models.CharField(max_length=100)
    participant_feedback = models.CharField(max_length=500)
    investigator_comment = models.CharField(max_length=500)
