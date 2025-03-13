from django.db import models


class ExitInterview(models.Model):

    subject_identifier = models.CharField(max_length=20)

    summary = models.TextField()

    investigator_observation = models.TextField()

    final_comments = models.TextField()

    final_recommendation = models.TextField()

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Exit Interview'
        verbose_name_plural = 'Exit Interviews'
