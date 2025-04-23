from django import forms
from ..models.compliance import ComplianceReport


class ComplianceForm(forms.ModelForm):

    class Meta:
        model = ComplianceReport
        fields = "__all__"
