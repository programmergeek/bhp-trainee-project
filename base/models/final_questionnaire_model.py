from django.db import models


class FinalQuestionnaire(models.Model):

    participant_identifier = models.CharField(max_length=50)
    participant_experience = models.CharField()
    perceived_benefits = models.CharField()
    perceived_challenges = models.CharField()
    willingness_to_participate_in_future_studies = models.CharField()
