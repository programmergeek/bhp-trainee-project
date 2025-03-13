from django import forms

from ..models.subject_visit import SubjectVisit


class SubjectVisitForm (forms.ModelForm):

    class Meta:
        model = SubjectVisit
        fields = '__all__'
