from django import forms
from ..models.subject_vitals import SubjectVitals


class SubjectVitalsForm(forms.ModelForm):

    class Meta:
        model = SubjectVitals
        fields = '__all__'
