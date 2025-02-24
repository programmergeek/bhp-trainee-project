from django.db import models


class ComplianceForm(models.Model):

    participant_identifier = models.CharField(max_length=50)
    dose_taken = models.CharField()
    dose_prescribed = models.CharField()
    participant_feedback = models.CharField()
    investigator_comment = models.CharField()
