from django.db import models


class AdverseEvent(models.Model):

    SEVERITY = (('mild', "Mild"), ('moderate', "Moderate"),
                ('severe', "Severe"))

    participant_identifier = models.CharField(max_length=50)
    severity = models.CharField(choices=SEVERITY, max_length=10)
    onset_date = models.DateField()
    resolution_date = models.DateField()
    action_taken = models.CharField(max_length=500)
    outcome = models.CharField(max_length=500)
    investigator_review = models.CharField(max_length=500)
