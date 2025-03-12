from django.db import models
from django.utils import timezone

from ..choices import ENROLLMENT_SITES, SEVERITY


class AdverseEvent(models.Model):

    subject_identifier = models.CharField(max_length=10)

    site = models.CharField(max_length=50, choices=ENROLLMENT_SITES)

    description = models.TextField()

    severity = models.CharField(max_length=20, choices=SEVERITY)

    onset_date = models.DateField(default=timezone.now())

    resolution_date = models.DateField()

    action_taken = models.TextField()

    outcome = models.TextField()

    investigator_review = models.TextField()

    investigator_comment = models.TextField()

    # This is an id for the investigator who performed the review and left the comment
    investigator_identifier = models.CharField(max_length=20)

    study_intervention_relationship = models.CharField(
        max_length=50,
        verbose_name='How related was the clinical study to the adverse event?'
    )

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Adverse Event'
        verbose_name_plural = 'Adverse Events'
