from django.db import models


class Compliance(models.Model):

    doses_taken = models.IntegerField()

    prescribed_dosage = models.IntegerField()

    subject_identifier = models.CharField(max_length=20)

    subject_feedback = models.TextField()

    investigator_comments = models.TextField()

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Compliance Form'
        verbose_name_plural = 'Compliance Forms'
