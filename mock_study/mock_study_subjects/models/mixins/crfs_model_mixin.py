from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from django.db import models
from ..subject_visit import SubjectVisit


class CrfModelMixin(
    BaseCrfModelMixin,
    ReferenceModelMixin,
    RequiresConsentFieldsModelMixin,
    PreviousVisitModelMixin,
    BaseUuidModel
):
    subject_visit = models.OneToOneField(
        SubjectVisit, on_delete=models.PROTECT)

    class Meta:
        abstract = True
