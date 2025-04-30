from django.db import models
from edc_base.model_mixins import BaseModel
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import SubjectIdentifierManager
from edc_action_item.model_mixins import ActionModelMixin
from edc_constants.choices import YES_NO
from ..action_items.final_questionnaire_action_item import FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME
from ..choices import EXPERIENCE_RATING, RATING_SCALE


class FinalQuestionnaire(BaseModel, ActionModelMixin):

    action_name = FINAL_QUESTIONNAIRE_ACTION_ITEM_NAME

    experience_rating = models.CharField(
        max_length=20,
        choices=EXPERIENCE_RATING,
        verbose_name='How would you describe your experience as a participant in the study?')

    study_purpose = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Do you believe that the purpose of the study was clearly explained to you?")

    study_purpose_grievance = models.TextField(
        blank=True,
        null=True,
        verbose_name="Please leave a comment on why you believe the purpose of the study was not clearly explained to you.")

    respectful_staff = models.CharField(
        max_length=3,
        choices=YES_NO, verbose_name="Do you believe that the staff was respectful and professional?")

    respectful_staff_comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="If you believe that the staff have not been respectful, please leave a comment as to why."
    )

    visit = models.CharField(
        max_length=20,
        choices=RATING_SCALE, verbose_name="Was the visit schedule easy for you to work with?")

    adherence = models.CharField(
        max_length=20,
        choices=RATING_SCALE, verbose_name="Did you find it easy to take your medication as instructed?")

    instruction_clearity = models.CharField(
        max_length=20,
        choices=RATING_SCALE, verbose_name="Do you believe the instructions given were simple to understand and follow?")

    instruction_clearity_grievance = models.TextField(
        verbose_name="Please state what about the instructions were not clear.", null=True, blank=True)

    benefits = models.TextField(
        verbose_name="What do you believe were the benefits of participating in this study?")

    challenges = models.TextField(
        verbose_name='What do you believe were the challenges you experiences because you were participating in this study?')

    paricipate_again = models.CharField(
        max_length=3,
        verbose_name="Would like to participate in any future studies we conduct?", choices=YES_NO)

    history = HistoricalRecords()

    objects = SubjectIdentifierManager()

    class Meta:
        app_label = 'mock_study_prn'
        verbose_name = "Final Questionnaire"
        verbose_name_plural = "Final Questionnaire"
