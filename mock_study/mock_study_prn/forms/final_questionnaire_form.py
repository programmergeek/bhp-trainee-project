from django import forms
from edc_form_validators import FormValidatorMixin
from mock_study_prn_validations.form_validators.final_questionnaire_validator import FinalQuestionnaireValidator
from ..models.final_questionnaire import FinalQuestionnaire


class FinalQuestionnaireForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = FinalQuestionnaireValidator

    class Meta:
        model = FinalQuestionnaire
        fields = "__all__"
