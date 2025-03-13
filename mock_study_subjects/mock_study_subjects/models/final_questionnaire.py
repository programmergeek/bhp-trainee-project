from django.db import models


class FinalQuestionnaire(models.Model):

    subject_identifier = models.CharField(max_length=20)

    participant_experience_with_the_study = models.TextField()

    percieved_benefits = models.TextField()

    percieved_challenges = models.TextField()

    willingness_to_participate_in_future_studies = models.CharField(
        max_length=20)

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Final Questionnaire'
        verbose_name_plural = 'Final Questionnaire'
