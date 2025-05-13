from django import forms

from ..models.response_to_drug import DrugResponse

class DrugResponseForm(forms.ModelForm):

    class Meta:
        model = DrugResponse
        fields = '__all__'
