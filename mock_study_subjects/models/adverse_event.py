from django.db import models


class AdverseEvent(models.Model):

    subject_identifier = models.CharField(max_length=10)

    site = models.CharField(max_length=50)

    description = models.TextField()

    severity = models.CharField(max_length=20)

    onset_date = models.DateField()

    resolution_date = models.DateField()

    action_taken = models.TextField()

    outcome = models.TextField()

    investigator_review = models.TextField()

    investigator_comment = models.TextField()

    study_intervention_relationship = models.CharField(
        max_length=50,
        verbose_name='How related was the clinical study to the adverse event?'
    )

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Adverse Event'
        verbose_name_plural = 'Adverse Events'
