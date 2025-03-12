from django import forms

from ..models.compliance import Compliance


class ComplianceForm(forms.ModelForm):

    class Meta:

        model = Compliance
        fields = '__all__'
