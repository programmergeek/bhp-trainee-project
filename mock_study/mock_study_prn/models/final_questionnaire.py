from django.db import models
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseModel
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import SubjectIdentifierManager
from edc_action_item.model_mixins import ActionModelMixin
from edc_constants.choices import YES_NO
from ..action_items.final_questionnaire_action_item import FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME
from ..choices import EXPERIENCE_RATING, RATING_SCALE


class FinalQuestionnaire(SiteModelMixin, BaseModel, ActionModelMixin):

    action_name = FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME

    experience_rating = models.TextField(
        choices=EXPERIENCE_RATING, verbose_name='How would you describe your experience as a participant in the study?')

    study_purpose = models.TextField(
        choices=YES_NO, verbose_name="Do you believe that the purpose of the study was clearly explained to you?")

    respectful_staff = models.TextField(
        choices=YES_NO, verbose_name="Do you believe that the staff was respectful and professional?")

    visit = models.TextField(
        choices=RATING_SCALE, verbose_name="Was the visit schedule easy for you to work with?")

    adherence = models.TextField(
        choices=RATING_SCALE, verbose_name="Did you find it easy to take your medication as instructed?")

    instruction_clearity = models.TextField(
        choices=RATING_SCALE, verbose_name="Do you believe the instructions given were simple to understand and follow. If you disagree, please state why.")

    instruction_clearity_grievance = models.TextField(
        verbose_name="Please state what about the instructions were not clear.", null=True, blank=True)

    history = HistoricalRecords()

    objects = SubjectIdentifierManager()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = "Final Questionnaire"
        verbose_name_plural = "Final Questionnaire"
