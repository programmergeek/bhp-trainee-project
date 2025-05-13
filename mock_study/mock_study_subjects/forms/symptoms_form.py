from django import forms

from ..models.symptoms import Symptoms

class SymptomsForm(forms.ModelForm):

    class Meta:
        model = Symptoms
        fields = '__all__'
