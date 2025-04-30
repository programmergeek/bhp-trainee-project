from django import forms
from edc_form_validators import FormValidatorMixin
from mock_study_prn_validations.form_validators.subject_offstudy_validator import SubjectOffStudyValidator
from ..models.subject_offstudy import SubjectOffStudy


class SubjectOffStudyForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectOffStudyValidator

    class Meta:
        model = SubjectOffStudy
        fields = "__all__"
