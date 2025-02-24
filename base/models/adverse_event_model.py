from django.db import models


class AdverseEvent(models.Model):

    SEVERITY = ["Mild", "Moderate", "Severe"]

    participant_identifier = models.CharField(max_length=50)
    severity = models.CharField(choices=SEVERITY)
    onset_date = models.DateField()
    resolution_date = models.DateField()
    action_taken = models.CharField()
    outcome = models.CharField()
    investigator_review = models.CharField()
