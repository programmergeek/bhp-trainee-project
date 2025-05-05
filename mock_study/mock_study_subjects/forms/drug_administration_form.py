from django import forms

from ..models.drug_administration import DrugAdministration


class DrugAdministrationForm(forms.ModelForm):

    class Meta:
        model = DrugAdministration
        fields = '__all__'
