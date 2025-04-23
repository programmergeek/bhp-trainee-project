from django import forms
from ..models.adverse_event_report import AdverseEventActionModel


class AdverseEventForm(forms.ModelForm):

    class Meta:
        model = AdverseEventActionModel
        fields = "__all__"
