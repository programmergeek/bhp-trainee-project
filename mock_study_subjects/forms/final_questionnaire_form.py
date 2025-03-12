from django import forms

from ..models.final_questionnaire import FinalQuestionnaire


class FinalQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = FinalQuestionnaire
        fields = '__all__'
