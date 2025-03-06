from django import forms

from ..models.subject_visit import SubjectVisit
from ..constants import UNSCHEDULED, INVALID_ERROR, MISSED_VISIT, OTHER


class VisitFormValidator:

    def validate_visit_code_sequence_and_reason(self):
        appointment = self.cleaned_data.get('appointment')
        reason = self.cleaned_data.get('reason')
        if appointment:
            if (appointment.visit_code not in ['1000']
                    and reason == UNSCHEDULED):
                raise forms.ValidationError({
                    'reason': 'Invalid. This is not an unscheduled visit'},
                    code=INVALID_ERROR)

    def validate_required_fields(self):

        self.required_if(
            MISSED_VISIT,
            field='reason',
            field_required='reason_missed')

        self.required_if(
            'Unscheduled visit/contact',
            field='reason',
            field_required='reason_unscheduled')

        self.required_if(
            OTHER,
            field='info_source',
            field_required='info_source_other')

        self.required_if(
            OTHER,
            field='reason_unscheduled',
            field_required='reason_unscheduled_other')


class SubjectVisitForm (forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
