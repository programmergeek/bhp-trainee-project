from django import forms
from ..models.death_reports import DeathReport


class DeathReportForm(forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = "__all__"
