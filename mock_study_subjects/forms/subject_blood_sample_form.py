from django import forms
from ..models.subject_blood_sample import SubjectBloodSample


class SubjectBloodSampleForm(forms.ModelForm):

    class Meta:
        form = SubjectBloodSample
        fields = '__all__'
