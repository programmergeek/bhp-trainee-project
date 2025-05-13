from django.db import models
from edc_constants.choices import YES_NO

from .mixins.crfs_model_mixin import CrfModelMixin
from ..choices import RATING_SCALE

class BaseRiskAssessmentDiet(CrfModelMixin):

    salty_foods = models.CharField(max_length=20, verbose_name='How often do you eat foods high in sodium and low in potassium, e.g polony, salty snacks, canned foods, etc?', choices=RATING_SCALE)

    saturated_fats = models.CharField(max_length=20, verbose_name='How often do you eat foods that have a lot of saturated fats, e.g fatty meats, butter, cheese, etc?', choices=RATING_SCALE)

    red_meats = models.CharField(max_length=20, verbose_name='How often do you eat red meat, e.g beef, goat, etc?', choices=RATING_SCALE)

    fruits_and_veg = models.CharField(max_length=3, verbose_name='Do you eat at least 4 servings of fruits and vegitables daily?', choices=YES_NO)

    grain = models.CharField(max_length=3, verbose_name='Do you have at least 6 servings of grain daily?', choices=YES_NO)

    nuts = models.CharField(max_length=3, verbose_name='Do you have at least 4 servings of nuts and seeds per week?', choices=YES_NO)

    low_fat_dairy = models.CharField(max_length=3, verbose_name="Do you have at least 2 servings of fat free or low fat dairy per day?", choices=YES_NO)

    class Meta(CrfModelMixin.Meta):
        app_label = 'mock_study_subjects'
        verbose_name = 'Base Risk Assessment: Diet'
        verbose_name_plural = 'Base Risk Assessment: Diet'
