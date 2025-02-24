from django.db import models


class FinalQuestionnaire(models.Model):

    CHOICES = (('unwilling', 'Unwilling'), ('moderatly_willing',
               'Moderate Willing'), ('very_willing', 'Very Willing'))

    participant_identifier = models.CharField(max_length=50)
    participant_experience = models.CharField(max_length=500)
    perceived_benefits = models.CharField(max_length=500)
    perceived_challenges = models.CharField(max_length=500)
    willingness_to_participate_in_future_studies = models.CharField(
        max_length=20, choices=CHOICES)
