from django.db import models


class LiverPanelBloodTestResult(models.Model):

    sample_identifier = models.CharField(max_length=20)

    test_date = models.CharField(max_length=20)

    status = models.CharField(max_length=10)

    alt = models.FloatField(verbose_name='Alanine Aminotransferase (ALT)')

    ast = models.FloatField(verbose_name='Aspartate Aminotransferase (AST)')

    alp = models.FloatField(verbose_name='Alkaline Phosphatase (ALP)')

    bilirubin_total = models.FloatField()

    bilirubin_direct = models.FloatField()

    bilirubin_indirect = models.FloatField()

    albumin = models.FloatField()

    total_protien = models.FloatField()

    class Meta:
        app_label = 'mock_study_subjects'
        verbose_name = 'Liver Pannel Blood Test Result'
        verbose_name_plural = 'Liver Pannel Blood Test Result'
