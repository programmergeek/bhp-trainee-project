from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from django.db import models
from django.db.models.deletion import PROTECT
from ..subject_visit import SubjectVisit


class CrfModelMixin(
    BaseCrfModelMixin,  # Defines all your base crf properties and methods
    # a mixin that gives you the ability to tell if the subject is on or off schedule
    SubjectScheduleCrfModelMixin,
    RequiresConsentFieldsModelMixin,  # makes subject consent required
    SiteModelMixin,
    BaseUuidModel
):
    '''
    A mixin for crf models
    '''
    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    class Meta:
        abstract = True
    pass
