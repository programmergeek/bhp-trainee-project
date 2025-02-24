from django.db import models


class ExitInterview(models.Model):

    participant_identifier = models.CharField(max_length=50)
    summary_of_parricipant_experience = models.CharField()
    investigator_observations = models.CharField()
    final_comments_and_recommendations = models.CharField()
