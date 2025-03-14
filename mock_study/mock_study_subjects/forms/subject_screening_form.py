from django import forms

from ..models.subject_screening import SubjectScreening


class SubjectScreeningForm(forms.ModelForm):

    class Meta:
        model = SubjectScreening
        fields = '__all__'
