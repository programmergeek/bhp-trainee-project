from django import forms
from ..models.subject_visit import SubjectVisit
from mock_study_subject_validations.form_validations.subject_visit_validator import VisitFormValidator
from edc_form_validators import FormValidatorMixin


class SubjectVisitForm (FormValidatorMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
