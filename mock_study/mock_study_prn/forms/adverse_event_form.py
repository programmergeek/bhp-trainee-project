from django import forms
from ..models.adverse_event_report import AdverseEvent


class AdverseEventForm(forms.ModelForm):

    class Meta:
        model = AdverseEvent
        fields = "__all__"
