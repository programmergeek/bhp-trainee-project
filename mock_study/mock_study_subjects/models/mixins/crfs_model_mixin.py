from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_base.model_mixins import BaseUuidModel
from django.db import models
from django.db.models.deletion import PROTECT
from ..subject_visit import SubjectVisit


class CrfModelMixin(
    BaseCrfModelMixin,  # Defines all your base crf properties and methods
    RequiresConsentFieldsModelMixin,  # makes subject consent required
    BaseUuidModel
):
    '''
    A mixin for crf models
    '''
    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    class Meta:
        abstract = True
    pass
